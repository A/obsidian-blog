# TODO: parse all includes in given markdown.
# If they contains another include, return children array

import glob
import os
import re
import frontmatter
from obsidian_blog.helpers import get_slug

from obsidian_blog.image import Image
from obsidian_blog.logger import log


MW_INCLUDE_REGEXP = r'(\[\[(.*)\]\])'

class Include:
  def __init__(self, placeholder, meta, content, includes, images):
    self.meta = meta
    self.content = content if meta.get("published") else ""
    self.includes = includes
    self.placeholder = placeholder
    self.images = images
    self.slug = get_slug(self)

  @staticmethod
  def get_all(content):
    return Include.get_includes(content)

  @staticmethod
  def get_includes(content: str):
    includes = []
    matches = re.findall(MW_INCLUDE_REGEXP, content)

    for match in matches:
      placeholder, filename = match
      # TODO: wmd has different syntax for images, shouldn't be here
      if Image.is_image(filename): continue
      try:
        filenames = glob.glob('**/' + filename + '.md', recursive=True)
        f = frontmatter.load(filenames[0])
        include = Include(
          placeholder=placeholder,
          content=f.content,
          meta=f.metadata,
          includes=Include.get_all(f.content),
          images=Image.get_all(f.content),

        )
        includes.append(include)
        log(f"- [PARSED]: {placeholder}")
      except:
        print(f"- [NOT FOUND] \"{placeholder}\"")

    return includes

  @staticmethod
  def render_all(parent, parent_content):
    for include in parent.includes:
      parent_content = include.render(parent, parent_content)
    return parent_content


  def render(self, parent, parent_content):
    self_content = self.content
    self_content = Include.render_all(self, self_content)
    self_content = Image.render_all(self, self_content)
    self_content = self.render_header(self_content)
    return parent_content.replace(self.placeholder, self_content)

  def render_header(self, self_content):
    title = self.meta.get("title")
    if title:
      header = "<h3 class='subheader' id='" + title + "'><a href='#" + title +"'>" + title  +"</a></h3>\n"
      self_content = f"{header}\n{self_content}"
    return self_content

