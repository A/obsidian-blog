from src.dataclasses.content_data import ContentData
from src.entities.inline_image import InlineImage
from tests.helpers import create_page


def test_markdown_image_parsing():
    placeholder = "![a](b.png)"
    page = create_page(content=placeholder, filename="page.md")

    entity = InlineImage.get_all(page)[0]

    assert entity.data.placeholder == placeholder
    assert entity.data.title == "b"
    assert entity.data.filename == "b.png"


def test_inline_image_rendering():
    placeholder = "![a](b.png)"
    page = create_page(content=placeholder, filename="page.md")

    asset_data = ContentData(
        placeholder=placeholder,
        filename="d.png",
    )

    entity = InlineImage(data=asset_data)
    res = entity.render(page.data)

    assert res == "![d](d.png)"
