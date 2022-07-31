import os
import pytest
import yaml
from src.lib import fs
from src.dataclasses.content_data import ContentData
from src.entities.obsidian_embed import ObsidianEmbed
from tests.helpers import create_page, get_fixture_path


@pytest.mark.parametrize("fixture_name", [("mediawiki_include")])
def test_obsidian_embed(snapshot, fixture_name):
    cwd = os.getcwd()
    fixture_path = get_fixture_path(fixture_name)
    page_path = f"{fixture_path}/page.md"
    os.chdir(fixture_path)

    filename, meta, content = fs.load(page_path)
    page = create_page(filename=filename, meta=meta, content=content)
    entities = ObsidianEmbed.get_all(page)
    assert len(entities) == 1

    entity = entities[0]
    snapshot.assert_match(yaml.dump(entity.data), f"{fixture_name}.yml")
    os.chdir(cwd)


def test_obsidian_embed_markdown_rendering():
    placeholder = "![[include]]"
    page = create_page(content=placeholder)

    content_data = ContentData(
        filename="include.md",
        placeholder=placeholder,
        content="abc",
    )
    entity = ObsidianEmbed(data=content_data)

    res = entity.render(page.data)

    assert res == "abc"


def test_obsidian_embed_image_rendering():
    placeholder = "![[include.png]]"
    page = create_page(content=placeholder)

    content_data = ContentData(
        filename="include.png",
        placeholder=placeholder,
    )
    entity = ObsidianEmbed(data=content_data)

    res = entity.render(page.data)

    assert res == "![include](include.png)"
