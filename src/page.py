import os
import frontmatter
from src.image import Image
from src.include import Include
from src import markdown, handlebars
from src.helpers import get_slug


class Page:
  @staticmethod
  def load(filename):
    page = frontmatter.load(filename)

    includes = []
    images = []

    if Page.is_md(filename):
      includes = Include.get_all(page.content)
      images = Image.get_all(page.content)

    return Page(
      filename = filename,
      meta = page.metadata,
      content = page.content,
      includes = includes,
      images = images,
    )

  def __init__(self, filename, meta, content, includes, images):
    self.filename = filename
    self.meta = meta
    self.content = content
    self.includes = includes
    self.images = images
    self.slug = get_slug(self)

  def get_content(self, content):
    return content

  @staticmethod
  def is_md(filename):
    _, ext = os.path.splitext(filename)
    return ext == ".md"

  def render(self, context):
    content = self.content
    if Page.is_md(self.filename):
      content = Image.render_all(self, content)
      content = Include.render_all(self, content)
      content = markdown.render(content)
    return handlebars.render_template(content, context)
