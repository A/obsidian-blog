from dataclasses import dataclass
import frontmatter
from src.image import Image
from src.include import Include
from src import markdown, handlebars
from src.helpers import get_slug, is_md
from src.logger import log
  
class Page:
  data: PageData
  included_files = []

  @staticmethod
  def load(filename):
    f = frontmatter.load(filename)
    return Page(filename, f.metadata, content = f.content)

  def __init__(self, filename, meta, content):
    self.filename = filename
    self.meta = meta
    self.content = ""
    self.images = []
    self.includes = []
    self.slug = get_slug(self)
    self.is_published = self.meta.get("published")
    self.is_md = is_md(filename)

    log(f"[PARSE]: {self.filename}")
    if not self.is_published:
      log(f"[SKIP]: Page {self.slug} is not published yet")
      return

    self.content = content
    if self.is_md:
      self.images = Image.get_all(content)
      self.includes = Include.get_all(content, self.included_files)

  def render(self, context = {}):
    content = self.content
    if is_md(self.filename):
      content = Image.render_all(self, content)
      content = Include.render_all(self, content)
      content = markdown.render(content)
    return handlebars.render_template(content, context)
