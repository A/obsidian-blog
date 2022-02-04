from src.models.page import PageModel
from src.parser.reference_image_parser import ReferenceImageParser


def test_reference_image_parser():

  content = """\
![Alt Title][id]

[id]: http://example.com
  """

  data = PageModel(content=content)
  parser = ReferenceImageParser()

  entities = parser.parse(data)
  entity = entities[0]

  assert(entity.parser_key == ReferenceImageParser.key)
  assert(entity.placeholder == "![Alt Title][id]")
  assert(entity.alt == "Alt Title")
  assert(entity.key == "id")
  assert(entity.filename == "http://example.com")
