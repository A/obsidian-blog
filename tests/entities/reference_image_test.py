from src.dataclasses.asset_data import AssetData
from src.entities.reference_image import ReferenceImage
from tests.helpers import create_page


def test_reference_image_parsing():
    placeholder = '![alt][image_id]'
    reference = '[image_id]: http://example.com'
    page = create_page(content=f'{placeholder}\n{reference}')

    entity = ReferenceImage.get_all(page)[0]

    assert entity.data.placeholder == placeholder
    assert entity.data.alt == 'alt'
    assert entity.data.key == 'image_id'
    assert entity.data.filename == 'http://example.com'


def test_reference_image_rendering():
    placeholder = '![alt][image_id]'
    reference = '![image_id]: http://example.com'
    page = create_page(content=f'{placeholder}\n{reference}')

    asset_data = AssetData(
        placeholder=placeholder,
        alt='new alt',
        filename='http://new-link.com',
        key='image_id',
    )

    entity = ReferenceImage(data=asset_data)
    res = entity.render(page.data)

    assert res == f'![new alt](http://new-link.com)\n{reference}'
