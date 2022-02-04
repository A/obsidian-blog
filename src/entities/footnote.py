# TODO: WRITE IT
import os
import re
import frontmatter
from slugify import slugify
from fs import basename, find_one_by_glob
from helpers import traverseBy
from src.logger import log

FOOTNOTE_REGEXP = r'(?<!^)(\[\[(.*)\]\])'

class Footnote:
  def __init__(self, filename, placeholder, meta, content, page):
    self.filename = filename
    self.placeholder = placeholder
    self.meta = meta
    self.page = page
    self.is_included = filename in page.included_files
    self.is_footnoted = filename in page.included_footnotes
    self.is_published = self.meta.get("published")
    self.footnote_content = ""

    log(f"[PARSE]: Footnote {self.placeholder}")
    if self.is_included:
      return 

    if self.is_footnoted:
      self.content = self.get_content(content)
      return

    self.footnote_content = content.split(r"^[-]{3,}")[0]
    return

  @property
  def title(self) -> str:
    if self.meta.get("title"):
      return self.meta.get("title")
    filename, _ = os.path.splitext(basename(self.filename))
    if " - " in filename:
      matches = re.findall(r"-(.*)\.\w+$", self.filename)
      return matches[0]
    return filename

  @property
  def id(self):
    return slugify(self.title)

  @property
  def content(self):
    if self.is_included:
      # TODO: should be a flat map of includes rather then a graph
      include = None
      search(page, "includes", lambda inc: inc.filename == self.filename)
      return 
    

  @staticmethod
  def load(filename, placeholder, page):
    f = frontmatter.load(filename)
    return Footnote(filename, placeholder, f.metadata, f.content, page)

  @staticmethod
  def get_all(content, page):
    return Footnote.get_footnote(content, included_files)

  @staticmethod
  def get_footnote(content: str, page):
    footnotes = []
    matches = re.findall(FOOTNOTE_REGEXP, content, flags=re.MULTILINE)

    for match in matches:
      placeholder, filename = match
      try:
        filename = find_one_by_glob(f"**/{filename}.md")
        footnote = Footnote.load(filename, placeholder, page)
        footnotes.append(footnote)
        log(f"- [PARSED]: {placeholder}")
      except Exception as e:
        print(f"- [NOT FOUND] \"{placeholder}\" {e}")

    return footnotes

