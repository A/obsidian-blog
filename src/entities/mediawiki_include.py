import os
import re
from slugify import slugify
import yaml
from src import fs
from src.dataclasses.content_data import ContentData
from src.fs import basename, find_one_by_glob
from src.logger import log


MW_INCLUDE_REGEXP = r'^(\[\[(.*)\]\])$'


class MediawikiInclude:
  def __init__(self, data: ContentData):
    self.data = data

  @staticmethod
  def get_all(entity):
    if not isinstance(entity.data, ContentData):
      return []

    includes = []
    matches = re.findall(MW_INCLUDE_REGEXP, entity.data.content, flags=re.MULTILINE)

    for match in matches:
      placeholder, filename = match
      try:
        filename = find_one_by_glob(f"**/{filename}.md")
        _, meta, content = fs.load(filename)

        data = ContentData(
          placeholder=placeholder,
          filename=filename,
          meta=meta,
          content=content
        )

        include = MediawikiInclude(data)

        includes.append(include)
        log(f"- [PARSED]: {placeholder}")
      except Exception as e:
        print(f"- [NOT FOUND] \"{placeholder}\" {e}")

    return includes

  @property
  def title(self) -> str:
    if self.data.meta.get("title"):
      return self.data.meta.get("title") or ""
    filename, _ = os.path.splitext(basename(self.data.filename))
    if " - " in filename:
      matches = re.findall(r"-(.*)\.\w+$", self.data.filename)
      return matches[0]
    return filename

  @property
  def id(self):
    return slugify(self.title)


  def render(self, data):
    content = data.content;
    return content.replace(self.data.placeholder, self.data.content)