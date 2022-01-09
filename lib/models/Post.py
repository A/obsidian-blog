from typing import TypedDict
from lib.models.Image import Image
from lib.models.Meta import Meta

Post = TypedDict('Post', {
  "file": str,
  "slug": str,
  "html": str,
  "meta": Meta,
  "imgs": list[Image],
})
