import os
from dataclasses import dataclass, field
from typing import Optional
from src.fs import basename
from slugify.slugify import slugify

TITLE_DELIMETER = " - "

@dataclass
class ContentData:
  filename: str = ""
  meta: dict = field(default_factory=dict)
  content: str = ""
  placeholder: Optional[str] = None
  entities: list = field(default_factory=list)

  @property
  def title(self):
    meta_title = self.meta.get("title")
    if isinstance(meta_title, str):
      return meta_title
    title, _ = os.path.splitext(basename(self.filename))
    if TITLE_DELIMETER in title:
      *_, title = title.split(TITLE_DELIMETER)
      return title
    return title

  @property
  def slug(self):
    meta_slug = self.meta.get("slug")
    if isinstance(meta_slug, str):
      return f"{meta_slug}.html"
    file, _ = os.path.splitext(self.filename)
    slug = slugify(os.path.basename(file))
    return f"{slug}.html"

  @property
  def id(self):
    filename, _ = os.path.splitext(self.filename)
    return slugify(filename)

  @property
  def ext(self):
    _, ext = os.path.splitext(self.filename)
    return ext

  @property
  def is_private(self):
    if self.meta.get("published"):
      return False
    return True

