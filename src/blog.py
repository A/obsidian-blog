import os
from src import config, fs
from src.dataclasses.content_data import ContentData
from src.entities.page import Page
from src.layout import Layout
from src.logger import log

class Blog():

  def __init__(self):
    log("\nParsing the blog content:")
    self.config = config
    self.layouts = self.load_layouts()
    self.posts = self.load_posts()
    self.pages = self.load_pages()

  def load_posts(self):
    """Returns all posts in the given directory"""
    posts = []
    posts_dir = self.config.POSTS_DIR
    files = fs.get_files_in_dir(posts_dir, filter_partials=True)
    for filename in files:
      filename, meta, content = fs.load(os.path.join(posts_dir, filename))
      data = ContentData(
        filename=filename,
        meta=meta,
        content=content
      )
      posts.append(Page(data))
    return sorted(posts, key=lambda post: post.data.meta.get("date"),  reverse=True)

  def load_layouts(self):
      layouts = {}
      layouts_dir = self.config.LAYOUTS_DIR

      files = fs.get_files_in_dir(layouts_dir, filter_partials=True)
      for file in files:
        layout = Layout(os.path.join(layouts_dir, file))
        layouts[layout.name] = layout
      return layouts

  def load_pages(self):
    pages = []
    pages_dir = self.config.PAGES_DIR
    files = fs.get_files_in_dir(pages_dir, filter_partials=True)
    for filename in files:
      filename, meta, content = fs.load(os.path.join(pages_dir, filename))
      data = ContentData(
        filename=filename,
        meta=meta,
        content=content
      )
      pages.append(Page(data))
    return pages

