import os
import pytest
from src import fs
from src.obsidian.page import Page
from tests.helpers import create_page, get_fixture_path


@pytest.mark.parametrize(
    'fixture_name',
    [
        ('page_nested'),
    ],
)
def test_page_nested(snapshot, fixture_name):
    cwd = os.getcwd()
    fixture_path = get_fixture_path(fixture_name)
    page_path = f'{fixture_path}/page.md'
    os.chdir(fixture_path)

    page = create_page(*fs.load(page_path))

    snapshot.assert_match(page.render(), f'{fixture_name}.html')
    os.chdir(cwd)


def test_page_get_all():
    cwd = os.getcwd()
    fixture_path = get_fixture_path('pages_dir')
    os.chdir(fixture_path)
    pages_dir = 'Pages'

    pages = Page.get_all(pages_dir)

    assert len(pages) == 3
    for page in pages:
        assert(page.data.content == page.data.filename)

    os.chdir(cwd)
