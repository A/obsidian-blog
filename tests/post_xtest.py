import pytest
from tests.helpers import get_fixture_path
from src.post import Post

@pytest.mark.parametrize("fixture_name", [
  "post",
  "post-image-inline",
  "post-mediawiki-image",
  "post-reference-image",
  "post-unpublished",
  "recursive-post",
])
def test_post_render(snapshot, fixture_name):
  fixture_path = get_fixture_path(fixture_name)
  post_path = f"{fixture_path}/post.md"

  post = Post.load(post_path)
  snapshot.assert_match(post.render(), fixture_name)
