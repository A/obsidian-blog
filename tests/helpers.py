import os
from src.dataclasses.content_data import ContentData
from src.obsidian.page import Page

fixtures_path = os.path.join(os.path.dirname(__file__), "__fixtures__")


def get_fixture_path(name: str):
    return os.path.join(fixtures_path, name)


def create_page(filename="page.md", meta=None, content=None):
    content_data = ContentData(filename=filename, meta=meta, content=content)
    return Page(data=content_data)


class DummyInclude:
    def __init__(self, data):
        self.data = data
