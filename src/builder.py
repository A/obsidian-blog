import os
import time

from slugify.slugify import slugify
from src import fs
from src.dataclasses.image_data import ImageData
from src.logger import log
from src.blog import Blog


class Builder():

  def build(self, timings):
    self.timings = timings
    self.blog = Blog()
    self.make_build_dir()
    self.copy_assets()
    self.render_all()

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
    log("\n# Prepare build\n")
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


  def render_all(self):
    entities = ['pages', 'posts']
    for entity in entities:
      log(f"\n# Render {entity}:\n")
      tic = time.perf_counter()
      for page in getattr(self.blog, entity):
        self.process_images(page)
        self.render(page)
      toc = time.perf_counter()
      self.timings[entity] = toc - tic

  def render(self, page):
    dest_dir = self.blog.config.DEST_DIR
    dest = os.path.join(dest_dir, page.data.slug)
    context = self.get_context({ "self": page.data })
    html = page.render_self(context)
    layout = self.get_layout(page)

    if layout is not None:
      html = layout.render(context | { "content": html })

    fs.write_file(dest, html)
    log("- [RENDERED]:", page.data.title)

  def get_layout(self, node):
    layout_name = node.data.meta.get("layout") or "main"
    return self.blog.layouts[layout_name]
  
  def process_images(self, page):
    for node in page.data.entities:
      entity = node.data
      data = entity.data
      if not issubclass(type(data), ImageData):
        continue
      try:
        dest_dir = self.blog.config.DEST_DIR
        assets_dest_dir = self.blog.config.ASSETS_DEST_DIR

        filename = data.filename
        file, ext = os.path.splitext(filename)
        to = f"{dest_dir}/{assets_dest_dir}/{slugify(file)}{ext}"
        url = f"/{assets_dest_dir}/{slugify(file)}{ext}"

        fs.copyfile(filename, to)
        data.filename = url
        log(f"- [COPY ASSET]: {filename} to {to}")
      except:
        # FIXME: Should skip abs paths and urls
        print("Something went wrong")

