from typing import TypedDict
from lib.models.Layout import Layout
from lib.models.Page import Page
from lib.models.Post import Post

BuilderContext = TypedDict('BuilderContext', {
  "config": dict[str, str],
  "layouts": dict[str, Layout],
  "posts": list[Post],
  "pages": list[Page],
})
