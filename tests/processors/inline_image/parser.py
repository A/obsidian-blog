from src.models.page import PageModel
from src.processors.inline_image import consts as c
from src.processors.inline_image.parser import InlineImageParser


def test_inline_image_parser():
  data = PageModel(content="![Alt Title](http://example.com)")
  parser = InlineImageParser()

  entities = parser.parse(data)
  entity = entities[0]

  assert(entity.parser_key == c.INLINE_IMAGE_PARSER_KEY)
  assert(entity.placeholder == "![Alt Title](http://example.com)")
  assert(entity.alt == "Alt Title")
  assert(entity.filename == "http://example.com")
