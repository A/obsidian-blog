from src.parser.parser_composer import ParserComposer
from src.builder.page_builder import PageBuilder
from src.models.page import PageModel

def test_page_builder():
  parser = ParserComposer([])
  data = PageModel(
    filename = "/test.md",
    meta = { "published": True },
    content = "Hello World",
  )
  page = PageBuilder(data, parser)
  assert(page.data == data)
