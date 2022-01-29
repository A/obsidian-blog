import os
import time

from slugify.slugify import slugify
from src import markdown, fs
from src.logger import log
from src.blog import Blog
from src.helpers import traverseBy


class Builder():

  def build(self, timings):
    self.timings = timings
    self.blog = Blog()
    self.make_build_dir()
    self.copy_assets()
    self.render_posts()
    self.render_pages()

  def get_context(self, local_ctx):
    global_ctx = {
      "config": {
        "BLOG_TITLE": self.blog.config.BLOG_TITLE,
        "ASSETS_PATH": "/" + self.blog.config.ASSETS_DEST_DIR,
      },
      "layouts": self.blog.layouts,
      "pages": self.blog.pages,
      "posts": self.blog.posts,
    }
    return global_ctx | local_ctx

  def make_build_dir(self):
    dest_dir = self.blog.config.DEST_DIR
    log(f"Prepare a build dir: {dest_dir}")
    fs.rm_dir(dest_dir)
    fs.make_dir(dest_dir)

  def copy_assets(self):
    dest_dir = self.blog.config.DEST_DIR
    assets_dir = self.blog.config.ASSETS_DIR
    assets_dest_dir = self.blog.config.ASSETS_DEST_DIR
    log(f"Copy assets from {assets_dir} to {dest_dir}/{assets_dest_dir}")
    dest_dir = self.blog.config.DEST_DIR
    fs.copy_dir(assets_dir, os.path.join(dest_dir, assets_dest_dir))

  def render_posts(self):
    log("\nRendering posts:")
    tic = time.perf_counter()
    for post in self.blog.posts:
      traverseBy("includes", post, lambda node: self.process_images(node))
      self.render_post(post)
    toc = time.perf_counter()
    self.timings["posts"] = toc - tic

  def render_post(self, post):
    if post.meta.get("published") == False:
      log("- [SKIPPED]:", post.meta.get("title"))
      return
    dest = os.path.join(self.blog.config.DEST_DIR, post.slug)
    html = markdown.render(post.render())
    layout = self.get_layout(post)
    context = self.get_context({ "self": self.create_entry_context(post), "content": html })

    if layout is not None:
      html = layout.render(context)

    fs.write_file(dest, html)
    log("- [RENDERED]:", post.meta.get("title"))

  def create_entry_context(self, entry):
    context = {}
    context["meta"] = entry.meta
    context["content"] = entry.content

    includes = []
    traverseBy("includes", entry, lambda node: includes.extend(node.includes))
    context["includes"] = list(filter(lambda include: include.is_published, includes))

    images = [*entry.images]
    traverseBy("images", entry, lambda node: includes.extend(node.images))
    context["images"] = images

    return context

  def get_layout(self, node):
    layout_name = node.meta.get("layout") or "main"
    return self.blog.layouts[layout_name]
  
  def process_images(self, node):
    if type(node.images) is not list: return
    for image in node.images:
      assets_dir = self.blog.config.ASSETS_DIR
      assets_dest_dir = self.blog.config.ASSETS_DEST_DIR

      frm = image.filename
      file, ext = os.path.splitext(image.filename)
      to = f"{assets_dir}/{slugify(file)}{ext}"
      url = f"/{assets_dest_dir}/{slugify(file)}{ext}"

      fs.copyfile(frm, to)
      image.filename = url
      log(f"- [COPY ASSET]: {frm} to {to}")

  def render_pages(self):
    log("\nRender pages:\n")
    tic = time.perf_counter()
    for page in self.blog.pages:
      traverseBy("includes", page, lambda node: self.process_images(node))
      self.render_page(page)
    toc = time.perf_counter()
    self.timings["pages"] = toc - tic

  def render_page(self, page):
    log("- [RENDERED]:", page.meta.get("title"))
    dest_dir = self.blog.config.DEST_DIR
    dest = os.path.join(dest_dir, page.slug)
    context = self.get_context({ "self": self.create_entry_context(page) })
    html = page.render(context)
    layout = self.get_layout(page)

    if layout is not None:
      html = layout.render(context | { "content": html })

    fs.write_file(dest, html)



