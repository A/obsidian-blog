from typing import Callable, TypedDict
from lib.models.Meta import Meta


Page = TypedDict('Page', {
  "file": str,
  "slug": str,
  "meta": Meta,
  "template": Callable,
})
