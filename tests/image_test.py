from tests.helpers import fakefs_setup, fakefs_teardown, mount_fixture
from src.image import Image

def test_inline_image():
  fakefs_setup()
  mount_fixture("images")

  content = "![image](./img.png)"
  result = Image.get_all(content)

  assert result[0].alt == "image"
  assert result[0].filename == "./img.png"

  fakefs_teardown()


def test_reference_image():
  content = """
    ![image][id]
    [id]: ./img.png
  """

  result = Image.get_all(content)
  
  assert result[0].alt == "image"
  assert result[0].filename == "./img.png"


def test_mediawiki_image():
  fs = fakefs_setup()
  fs.create_file("/vault/image.png")

  content = "![[image.png]]"
  result = Image.get_all(content)
  
  assert result[0].alt == "image.png"
  assert result[0].filename == "vault/image.png"

  fakefs_teardown()

