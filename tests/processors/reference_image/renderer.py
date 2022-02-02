from src.processors.reference_image.entity import ReferenceImageEntity
from src.processors.reference_image.renderer import ReferenceImageRenderer

def test_inline_image_renderer():
  placeholder = "[alt][image_id]"
  reference = "[image_id]: http://example.com"
  content = f"text\n{placeholder}\n{reference}"

  entity = ReferenceImageEntity(
    placeholder=placeholder, 
    alt="new alt",
    filename="http://new-link.com",
    key="image_id"
  )

  renderer = ReferenceImageRenderer()
  res = renderer.render(content, entity)

  assert(res == f"text\n[new alt](http://new-link.com)\n{reference}")
