import os
import time
from src import fs
from src.dataclasses.asset_data import AssetData
from src.dataclasses.config_data import ConfigData
from src.logger import log
from src.blog import Blog


class Builder():

  def build(self, timings, config: ConfigData):
    self.timings = timings
    self.config = config
    self.blog = Blog()

    print("\n# Prepare build:")
    self.make_build_dir()
    self.copy_assets()

    print("")
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
    print(f"- Prepare a build dir: {dest_dir}")
    fs.rm_dir(dest_dir)
    fs.make_dir(dest_dir)

  def copy_assets(self):
    dest_dir = self.blog.config.DEST_DIR
    assets_dir = self.blog.config.ASSETS_DIR
    assets_dest_dir = self.blog.config.ASSETS_DEST_DIR
    print(f"- Copy assets from {assets_dir} to {dest_dir}/{assets_dest_dir}")
    dest_dir = self.blog.config.DEST_DIR
    fs.copy_dir(assets_dir, os.path.join(dest_dir, assets_dest_dir))


  def render_all(self):
    entities = ['pages', 'posts']
    for entity in entities:
      print(f"# Render {entity}:")
      tic = time.perf_counter()

      pages = getattr(self.blog, entity)
      for page in getattr(self.blog, entity):
        print(f"- {page.data.title}")
        self.process_images(page)
        self.render(page)

      toc = time.perf_counter()

      print("")
      print(f"{len(pages)} {entity} have been rendered in {toc-tic:0.4f} seconds\n")


  def render(self, page):
    dest_dir = self.blog.config.DEST_DIR
    dest = os.path.join(dest_dir, page.data.slug)
    context = self.get_context({ "self": page.data })
    html = page.render_self(context)
    layout = self.get_layout(page)

    if layout is not None:
      html = layout.render(context | { "content": html })

    fs.write_file(dest, html)

  def get_layout(self, node):
    layout_name = node.data.meta.get("layout") or "main"
    return self.blog.layouts[layout_name]
  
  def process_images(self, page):
    for node in page.data.entities:
      entity = node.data
      asset_data = entity.data

      if not issubclass(type(asset_data), AssetData):
        continue

      try:
        dest_dir = self.blog.config.DEST_DIR
        assets_dest_dir = self.blog.config.ASSETS_DEST_DIR
        dest_filename = f"{asset_data.id}{asset_data.ext}"

        frm = asset_data.filename
        to = f"{dest_dir}/{assets_dest_dir}/dest_filename"
        url = f"/{assets_dest_dir}/{dest_filename}"

        fs.copyfile(frm, to)
        asset_data.filename = url
        print(f"  - [COPY ASSET]: {frm} to {to}")

      except:
        # FIXME: Should skip abs paths and urls
        pass

