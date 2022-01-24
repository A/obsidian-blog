import frontmatter
from src.tests.helpers import fakefs_setup, fakefs_teardown, mount_fixture
from src.post import Post

def test_post_render():
  fakefs_setup()
  path = mount_fixture("post")

  post_path = f"{path}/post.md"
  post = Post.load(post_path)
  snapshot = frontmatter.load(f"{post_path}.snapshot")
  assert post.render() == snapshot.content
  fakefs_teardown()

