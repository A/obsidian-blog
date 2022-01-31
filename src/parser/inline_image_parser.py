import re
from src.models.page import PageModel

PARSER_KEY = "inline-image-entity"
MD_INLINE_IMG_REGEXP = r'(\!\[(.*)\]\((.*)\))'

class InlineImageEntry:
  parser_key = PARSER_KEY

  def __init__(self, placeholder, alt, filename):
    self.placeholder = placeholder
    self.alt = alt
    self.filename = filename


class InlineImageParser():
  key = PARSER_KEY

  def parse(self, data: PageModel):
    parent_content = data.content
    matches = re.findall(MD_INLINE_IMG_REGEXP, parent_content)
    return list(map(lambda match: InlineImageEntry(*match), matches))
