import os
import pytest
import yaml
from src.entities.mediawiki_link import MediawikiIncludeLink
from src.lib import fs
from tests.helpers import create_page, get_fixture_path


@pytest.mark.parametrize('fixture_name', [('mediawiki_links')])
def test_mediawiki_inlude(snapshot, fixture_name):
    cwd = os.getcwd()
    fixture_path = get_fixture_path(fixture_name)
    os.chdir(fixture_path)
    page_path = f'{fixture_path}/page.md'

    filename, meta, content = fs.load(page_path)
    page = create_page(filename=filename, meta=meta, content=content)
    entities = MediawikiIncludeLink.get_all(page)

    assert len(entities) == 3
    snapshot.assert_match(yaml.dump(page.render()), f'{fixture_name}.yml')

    os.chdir(cwd)
