from src.entities.page import Page, PageData

def test_page_creation():
  data = PageData(
    filename = "/test.md",
    meta = { "published": True },
    content = "Hello World",
  )
  page = Page(data)
  assert(page.data == data)

def test_page_processing():
  data = PageData(
    filename = "/test.md",
    meta = { "published": True },
    content = "Hello World ![a](b)",
  )
  page = Page(data)
  
  # Image is parsed
  assert(len(page.data.entities) == 1)
