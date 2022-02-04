from src.models.page import PageModel
from src.entities.inline_image import InlineImage


def test_inline_image_parsing():
  data = PageModel(content="![Alt Title](http://example.com)")

  entities = InlineImage.get_all(data)
  entity = entities[0]

  assert(entity.placeholder == "![Alt Title](http://example.com)")
  assert(entity.alt == "Alt Title")
  assert(entity.filename == "http://example.com")


def test_inline_image_rendering():
  placeholder = "[Link](http://example.com)"
  data = PageModel(
    content = f"text\n{placeholder}"
  )

  entity = InlineImage(
    placeholder=placeholder, 
    alt="New Link",
    filename="http://new-link.com",
  )

  res = InlineImage.render_one(data, entity)

  assert(res == "text\n[New Link](http://new-link.com)")
