from typing import TypedDict

IncludeMeta = TypedDict('IncludeMeta', {
  "title": str,
})

Include = TypedDict('Include', {
  "file": str,
  "name": str,
  "meta": IncludeMeta,
  "content": str,
  "placeholder": str,
})
