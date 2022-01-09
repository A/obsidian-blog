from typing import Callable, TypedDict


Layout = TypedDict('Layout', {
  "name": str,
  "template": Callable,
})
