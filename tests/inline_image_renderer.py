from src.parser.inline_image_parser import InlineImageEntry
from src.renderer.inline_image_renderer import InlineImageRenderer

def test_inline_image_renderer():
  placeholder = "[Link](http://example.com)"
  content = f"text\n{placeholder}"

  entity = InlineImageEntry(
    placeholder=placeholder, 
    alt="New Link",
    filename="http://new-link.com",
  )

  renderer = InlineImageRenderer()
  res = renderer.render(content, entity)

  assert(res == "text\n[New Link](http://new-link.com)")
