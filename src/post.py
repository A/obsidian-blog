import frontmatter
from src.helpers import get_slug
from src.image import Image
from src.include import Include
from src.logger import log

class Post():
  included_files = []

  @staticmethod
  def load(filename):
    f = frontmatter.load(filename)
    return Post(filename, f.metadata, f.content)

  def __init__(self, filename, meta, content):
    self.filename = filename
    self.meta = meta
    self.content = ""
    self.images = []
    self.includes = []
    self.slug = get_slug(self)
    self.is_published = self.meta.get("published")
    
    log(f"[PARSE]: {self.filename}")
    if not self.is_published:
      log(f"[SKIP]: Post {self.filename} is not published yet")
      return

    self.content = content
    self.images = Image.get_all(self.content)
    self.includes = Include.get_all(self.content, self.included_files)
  

  def render(self):
    content = self.content
    content = Image.render_all(self, content)
    content = Include.render_all(self, content)
    return content
