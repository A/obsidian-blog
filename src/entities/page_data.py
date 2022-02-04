import re
import os
from dataclasses import dataclass, field
from src.fs import basename
from src.helpers import get_slug, is_md

@dataclass
class PageData:
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
    return get_slug(self)

  @property
  def is_md(self):
    return is_md(self.filename)
