from src.dataclasses.content_data import ContentData
from src.preprocessors.include_header import IncludeHeaderPreprocessor
from tests.helpers import DummyInclude

def test_include_header_preprocessor():
  content_data = ContentData(
    filename="a.md",
    meta={ "title": "abc" },
    content="content",
  )

  entity = DummyInclude(content_data)
  IncludeHeaderPreprocessor.process(entity)

  entity.data.content
  
  assert(content_data.content == f"<h2 id=\"a\">abc</h2>\ncontent")
