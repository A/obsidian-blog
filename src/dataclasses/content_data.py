import re
import os
from dataclasses import dataclass, field
from typing import Optional
from src.fs import basename
from slugify.slugify import slugify

@dataclass
class ContentData:
  placeholder: Optional[str] = None
  filename: str = ""
  meta: dict = field(default_factory=dict)
  content: str = ""
  entities: list = field(default_factory=list)

  @property
  def title(self):
    if self.meta.get("title"):
      return self.meta.get("title")
    filename, _ = os.path.splitext(basename(self.filename))
    if " - " in filename:
      matches = re.findall(r"-(.*)\.\w+$", self.filename)
      return matches[0]
    return filename

  @property
  def slug(self):
    file, _ = os.path.splitext(self.filename)
    slug = slugify(os.path.basename(file))
    if self.meta.get("slug"):
      slug = self.meta.get("slug")
    return f"{slug}.html"

  @property
  def is_md(self):
    _, ext = os.path.splitext(self.filename)
    return ext == ".md"
