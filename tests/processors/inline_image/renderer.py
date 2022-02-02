from src.processors.inline_image.entity import InlineImageEntity
from src.processors.inline_image.renderer import InlineImageRenderer

def test_inline_image_renderer():
  placeholder = "[Link](http://example.com)"
  content = f"text\n{placeholder}"

  entity = InlineImageEntity(
    placeholder=placeholder, 
    alt="New Link",
    filename="http://new-link.com",
  )

  renderer = InlineImageRenderer()
  res = renderer.render(content, entity)

  assert(res == "text\n[New Link](http://new-link.com)")
