import os
import re
import frontmatter
from slugify import slugify
from src.fs import basename, find_one_by_glob
from src.helpers import get_slug

from src.image import Image
from src.logger import log


MW_INCLUDE_REGEXP = r'^(\[\[(.*)\]\])'

class Include:
  def __init__(self, filename, placeholder, meta, content, included_files):
    self.filename = filename
    self.placeholder = placeholder
    self.meta = meta
    self.content = ""
    self.includes = []
    self.images = []
    self.slug = get_slug(self)
    self.is_included = filename in included_files
    self.is_published = self.meta.get("published")

    included_files.append(filename)

    log(f"[PARSE]: {self.placeholder}")
    if self.is_included:
      log(f"[SKIP]: Include {self.placeholder} has been included already")
      self.content = f"[{self.title}](#{self.id})"
      return
    
    if not self.is_published:
      log(f"[SKIP] Include {self.placeholder} is not published yet")
      return

    self.content = content
    self.includes = Include.get_all(self.content, included_files)
    self.images = Image.get_all(self.content)

  @staticmethod
  def get_includes(content: str, included_files):
    includes = []
    matches = re.findall(MW_INCLUDE_REGEXP, content, flags=re.MULTILINE)

    for match in matches:
      placeholder, filename = match
      # TODO: wmd has different syntax for images, shouldn't be here
      if Image.is_image(filename): continue
      try:
        filename = find_one_by_glob(f"**/{filename}.md")
        include = Include.load(filename, placeholder, included_files)
        includes.append(include)
        log(f"- [PARSED]: {placeholder}")
      except Exception as e:
        print(f"- [NOT FOUND] \"{placeholder}\" {e}")

    return includes

  @staticmethod
  def load(filename, placeholder, included_files):
    f = frontmatter.load(filename)
    return Include(filename, placeholder, f.metadata, f.content, included_files)

  @staticmethod
  def get_all(content, included_files):
    return Include.get_includes(content, included_files)

  @staticmethod
  def render_all(parent, parent_content):
    for include in parent.includes:
      parent_content = include.render(parent, parent_content)
    return parent_content
  
  @property
  def id(self):
    return slugify(self.title)

  @property
  def title(self):
    if self.meta.get("title"):
      return self.meta.get("title")
    filename, _ = os.path.splitext(basename(self.filename))
    if " - " in filename:
      matches = re.findall(r"-(.*)\.\w+$", self.filename)
      return matches[0]
    return filename

  def render(self, parent, parent_content):
    self_content = self.content
    self_content = Include.render_all(self, self_content)
    self_content = Image.render_all(self, self_content)
    self_content = self.render_header(self_content)
    return parent_content.replace(self.placeholder, self_content)

  def render_header(self, self_content):
    header = "<h3 class='subheader' id='" + self.id + "'><a href='#" + self.id +"'>" + self.title  +"</a></h3>\n"
    self_content = f"{header}\n{self_content}"
    return self_content

