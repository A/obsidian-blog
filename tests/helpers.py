import os

fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')

def get_fixture_path(name: str):
   return os.path.join(fixtures_path, name)
