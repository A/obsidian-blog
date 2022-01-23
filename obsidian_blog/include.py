# TODO: parse all includes in given markdown.
# If they contains another include, return children array

import glob
import os
import re
import frontmatter

from obsidian_blog.image import Image


MW_INCLUDE_REGEXP = r'(\[\[(.*)\]\])'

class Include:
  def __init__(self, placeholder, meta, content, includes, images):
    self.meta = meta
    self.content = content
    self.includes = includes
    self.placeholder = placeholder
    self.images = images

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
      except:
        print(f"Include \"{placeholder}\" not found")

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
    return parent_content.replace(self.placeholder, self_content)
