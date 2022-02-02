from src.models.page import PageModel
from src.processors.reference_image.parser import ReferenceImageParser
from src.processors.reference_image import consts as c


def test_reference_image_parser():

  content = """\
![Alt Title][id]

[id]: http://example.com
  """

  data = PageModel(content=content)
  parser = ReferenceImageParser()

  entities = parser.parse(data)
  entity = entities[0]

  assert(entity.parser_key == c.REFERENCE_IMAGE_PARSER_KEY)
  assert(entity.placeholder == "![Alt Title][id]")
  assert(entity.alt == "Alt Title")
  assert(entity.key == "id")
  assert(entity.filename == "http://example.com")

