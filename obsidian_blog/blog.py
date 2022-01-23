import os
from obsidian_blog import config, fs
from obsidian_blog.layout import Layout
from obsidian_blog.logger import log
from obsidian_blog.page import Page
from obsidian_blog.post import Post

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
    source_dir = self.config.SOURCE_DIR
    files = fs.get_files_in_dir(source_dir, filter_partials=True)
    for file in files:
      post = Post.load(os.path.join(source_dir, file))
      posts.append(post)
    return sorted(posts, key=lambda post: post.meta.get("date"),  reverse=True)

  def load_layouts(self):
      layouts = {}
      layouts_dir = self.config.LAYOUTS_DIR

      files = fs.get_files_in_dir(layouts_dir, filter_partials=True)
      for file in files:
        layout = Layout(os.path.join(layouts_dir, file))
        layouts[layout.name] = layout
      return layouts

  def load_pages(self):
    pages: list[Page] = []
    pages_dir = self.config.PAGES_DIR
    files = fs.get_files_in_dir(pages_dir, filter_partials=True)
    for file in files:
      page = Page(os.path.join(pages_dir, file))
      pages.append(page)
    return pages

