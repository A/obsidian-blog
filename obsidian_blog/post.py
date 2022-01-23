# TODO: Image data structure should be updated before render
# Builder can copy files, then update url, and call render

import frontmatter

from obsidian_blog.image import Image
from obsidian_blog.include import Include


class Post():
  private: bool
  content: str = ""

  @staticmethod
  def load(path):
    f = frontmatter.load(path)
    return Post(
      meta=f.metadata,
      content=f.content,
      images=Image.get_all(f.content),
      includes=Include.get_all(f.content),
    )

  def __init__(self, meta, content, images, includes):
    self.meta = meta
    self.content = content
    self.images = images
    self.includes = includes

  def render(self):
    content = self.content
    content = Image.render_all(self, content)
    content = Include.render_all(self, content)
    return content
