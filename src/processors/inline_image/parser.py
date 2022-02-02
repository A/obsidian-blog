import re
from src.models.page import PageModel
from src.processors.inline_image import consts as c
from src.processors.inline_image.entity import InlineImageEntity

class InlineImageParser():
  key = c.INLINE_IMAGE_PARSER_KEY

  def parse(self, data: PageModel):
    parent_content = data.content
    matches = re.findall(c.MD_INLINE_IMG_REGEXP, parent_content)
    return list(map(lambda match: InlineImageEntity(*match), matches))

