from src.dataclasses.image_data import ImageData
from src.entities.reference_image import ReferenceImage
from tests.helpers import create_page


def test_reference_image_parsing():
  placeholder = "![alt][image_id]"
  reference = "[image_id]: http://example.com"
  page = create_page(f"{placeholder}\n{reference}")

  entity = ReferenceImage.get_all(page)[0]

  assert(entity.data.placeholder == placeholder)
  assert(entity.data.alt == "alt")
  assert(entity.data.key == "image_id")
  assert(entity.data.filename == "http://example.com")


def test_reference_image_rendering():
  placeholder = "![alt][image_id]"
  reference = "![image_id]: http://example.com"
  page = create_page(f"{placeholder}\n{reference}")

  image_data = ImageData(
    placeholder=placeholder, 
    alt="new alt",
    filename="http://new-link.com",
    key="image_id"
  )

  entity = ReferenceImage(data=image_data)
  res = entity.render(page)

  assert(res == f"![new alt](http://new-link.com)\n{reference}")
