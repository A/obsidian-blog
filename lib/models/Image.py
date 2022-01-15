from typing import TypedDict

Image = TypedDict('Image', {
  "file": str,
  "slug": str,
  "name": str,
  "placeholder": str,
})
