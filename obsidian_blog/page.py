import os
import frontmatter
from obsidian_blog import markdown, handlebars
from obsidian_blog.helpers import get_slug


class Page:

  def __init__(self, filename):
    page = frontmatter.load(filename)
    self.filename = filename
    self.meta = page.metadata
    self.content = self.get_content(page.content)
    self.slug = get_slug(self)
    self.template_fn = handlebars.create_template_fn(self.content)

  def get_content(self, content):
    _, ext = os.path.splitext(self.filename)
    if ext == ".md": content = markdown.parse(content)
    return content

  def render(self, context):
    return self.template_fn(context)
