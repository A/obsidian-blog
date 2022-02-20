from src.dataclasses.content_data import ContentData
from src.entities.reference_image import ReferenceImage
from tests.helpers import create_page


def test_reference_image_parsing():
    placeholder = '![alt][image_id]'
    reference = '[image_id]: http://example.com'
    page = create_page(content=f'{placeholder}\n{reference}')

    entity = ReferenceImage.get_all(page)[0]

    assert entity.data.placeholder == placeholder
    assert entity.data.filename == 'http://example.com'


def test_reference_image_rendering():
    placeholder = '![alt][image_id]'
    reference = '![image_id]: image.png'
    page = create_page(content=f'{placeholder}\n{reference}')

    content_data = ContentData(
        placeholder=placeholder,
        filename='new-image.png',
    )

    entity = ReferenceImage(data=content_data)
    res = entity.render(page.data)

    assert res == f'![new-image](new-image.png)\n{reference}'
