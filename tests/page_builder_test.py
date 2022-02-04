from src.builder.page import Page
from src.models.page import PageModel

def test_page_creation():
  data = PageModel(
    filename = "/test.md",
    meta = { "published": True },
    content = "Hello World",
  )
  page = Page(data)
  assert(page.data == data)

def test_page_processing():
  data = PageModel(
    filename = "/test.md",
    meta = { "published": True },
    content = "Hello World ![a](b)",
  )
  page = Page(data)
  
  # Image is parsed
  assert(len(page.data.entities) == 1)
