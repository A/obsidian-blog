import frontmatter
from src.page import Page
from tests.helpers import fakefs_setup, fakefs_teardown, mount_fixture

def test_page_render():
  fakefs_setup()
  path = mount_fixture("page")

  post_path = f"{path}/page.hbs"
  page = Page.load(post_path)
  snapshot = frontmatter.load(f"{post_path}.snapshot")
  assert page.render({}) == snapshot.content
  fakefs_teardown()


def test_page_md_render():
  fakefs_setup()
  path = mount_fixture("page-md")

  post_path = f"{path}/page.md"
  page = Page.load(post_path)
  snapshot = frontmatter.load(f"{post_path}.snapshot")
  print(page.render({}))
  assert page.render({}) == snapshot.content
  fakefs_teardown()

