from src.models.page import PageModel
from src.processors.reference_image import ReferenceImage


def test_reference_image_parsing():
  placeholder = "![alt][image_id]"
  reference = "[image_id]: http://example.com"
  content = f"{placeholder}\n{reference}"
  data = PageModel(content=content)

  entity = ReferenceImage.get_all(data)[0]

  assert(entity.placeholder == placeholder)
  assert(entity.alt == "alt")
  assert(entity.key == "image_id")
  assert(entity.filename == "http://example.com")


def test_inline_image_rendering():
  placeholder = "![alt][image_id]"
  reference = "![image_id]: http://example.com"
  content = f"{placeholder}\n{reference}"
  data = PageModel(content=content)

  entity = ReferenceImage(
    placeholder=placeholder, 
    alt="new alt",
    filename="http://new-link.com",
    key="image_id"
  )

  res = ReferenceImage.render_one(data, entity)

  assert(res == f"![new alt](http://new-link.com)\n{reference}")
