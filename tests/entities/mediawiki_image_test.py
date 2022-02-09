import os
import pytest
from src.lib import fs
from src.dataclasses.asset_data import AssetData
from src.entities.mediawiki_image import MediawikiImage
from tests.helpers import create_page, get_fixture_path


@pytest.mark.parametrize('fixture_name', [('mediawiki_image')])
def test_mediawiki_image_parsing(fixture_name):
    cwd = os.getcwd()
    fixture_path = get_fixture_path(fixture_name)
    page_path = f'{fixture_path}/page.md'
    os.chdir(fixture_path)

    filename, meta, content = fs.load(page_path)
    page = create_page(filename=filename, meta=meta, content=content)
    entities = MediawikiImage.get_all(page)
    assert len(entities) == 1

    entity = entities[0]

    assert entity.data.placeholder == '![[image.png]]'
    assert entity.data.alt == 'image.png'
    assert entity.data.key == None
    assert entity.data.filename == 'image.png'

    os.chdir(cwd)


def test_mediawiki_image_rendering():
    placeholder = '![[a]]'
    page = create_page(content=placeholder)

    asset_data = AssetData(
        placeholder=placeholder,
        alt='c',
        filename='d',
    )

    entity = MediawikiImage(data=asset_data)
    res = entity.render(page.data)

    assert res == '![c](d)'
