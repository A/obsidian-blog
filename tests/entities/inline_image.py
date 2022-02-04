from src.entities.inline_image import InlineImage
from src.entities.page import Page


def test_inline_image_parsing():
  data = Page(content="![Alt Title](http://example.com)")

  entities = InlineImage.get_all(data)
  entity = entities[0]

  assert(entity.placeholder == "![Alt Title](http://example.com)")
  assert(entity.alt == "Alt Title")
  assert(entity.filename == "http://example.com")


def test_inline_image_rendering():
  placeholder = "[Link](http://example.com)"
  data = Page(
    content = f"text\n{placeholder}"
  )

  entity = InlineImage(
    placeholder=placeholder, 
    alt="New Link",
    filename="http://new-link.com",
  )

  res = InlineImage.render_one(data, entity)

  assert(res == "text\n[New Link](http://new-link.com)")
