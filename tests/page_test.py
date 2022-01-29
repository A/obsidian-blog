import pytest
from tests.helpers import get_fixture_path
from src.page import Page

@pytest.mark.parametrize("fixture_name,filename", [
  ("page-hbs", "page.hbs"),
  ("page-md", "page.md"),
])
def test_page_render(snapshot, fixture_name, filename):
  fixture_path = get_fixture_path(fixture_name)
  post_path = f"{fixture_path}/{filename}"

  page = Page.load(post_path)
  snapshot.assert_match(page.render(), filename)
