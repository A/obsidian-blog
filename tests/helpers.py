import os
from src.dataclasses.content_data import ContentData
from src.entities.page import Page

fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')

def get_fixture_path(name: str):
   return os.path.join(fixtures_path, name)

def create_page(content: str):
  content_data = ContentData(content=content)
  return Page(data=content_data)

