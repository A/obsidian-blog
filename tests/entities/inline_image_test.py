from src.dataclasses.image_data import ImageData
from src.entities.inline_image import InlineImage
from tests.helpers import create_page


def test_inline_image_parsing():
  placeholder = "![a](b)"
  page = create_page(content=placeholder)

  entity = InlineImage.get_all(page)[0]

  assert(entity.data.placeholder == placeholder)
  assert(entity.data.alt == "a")
  assert(entity.data.key == None)
  assert(entity.data.filename == "b")


def test_inline_image_rendering():
  placeholder = "![a](b)"
  page = create_page(content=placeholder)

  image_data = ImageData(
    placeholder=placeholder, 
    alt="c",
    filename="d",
  )

  entity = InlineImage(data=image_data)
  res = entity.render(page.data)

  assert(res == "![c](d)")
