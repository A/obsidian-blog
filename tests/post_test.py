import frontmatter
from tests.helpers import fakefs_setup, fakefs_teardown, mount_fixture
from src.post import Post

def test_private_post_render():
  fakefs_setup()
  path = mount_fixture("post-unpublished")
  post_path = f"{path}/post.md"

  post = Post.load(post_path)
  assert post.render() == ""
  assert len(post.includes) == 0
  assert len(post.images) == 0

  fakefs_teardown()


def test_post_render():
  fakefs_setup()
  path = mount_fixture("post")
  post_path = f"{path}/post.md"
  snapshot = frontmatter.load(f"{post_path}.snapshot")

  post = Post.load(post_path)
  assert post.render() == snapshot.content

  fakefs_teardown()

def test_recursive_post_render():
  fakefs_setup()
  path = mount_fixture("recursive-post")
  post_path = f"{path}/post.md"
  snapshot = frontmatter.load(f"{post_path}.snapshot")

  post = Post.load(post_path)
  assert post.render() == snapshot.content
  fakefs_teardown()

