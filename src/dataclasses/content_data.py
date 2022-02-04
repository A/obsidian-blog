import re
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
    if self.meta.get("title"):
      return self.meta.get("title")
    title, _ = os.path.splitext(basename(self.filename))
    if TITLE_DELIMETER in title:
      *_, title = title.split(TITLE_DELIMETER)
      return title
    return title

  @property
  def slug(self):
    if self.meta.get("slug"):
      slug = self.meta.get("slug")
      return f"{slug}.html"

    file, _ = os.path.splitext(self.filename)
    slug = slugify(os.path.basename(file))
    return f"{slug}.html"

  @property
  def is_md(self):
    _, ext = os.path.splitext(self.filename)
    return ext == ".md"

  @property
  def is_private(self):
    if self.meta.get("published"):
      return False
    return True

