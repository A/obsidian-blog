from src.models.page import PageModel
from src.parser.inline_image_parser import InlineImageParser


def test_inline_image_parser():
  data = PageModel(content="![Alt Title](http://example.com)")
  parser = InlineImageParser()

  entities = parser.parse(data)
  entity = entities[0]

  assert(entity.parser_key == InlineImageParser.key)
  assert(entity.placeholder == "![Alt Title](http://example.com)")
  assert(entity.alt == "Alt Title")
  assert(entity.filename == "http://example.com")
