from dataclasses import dataclass, field
from src.helpers import get_slug

@dataclass
class IncludeData:
  placeholder: str
  filename: str
  meta: dict = field(default_factory=dict)
  content: str = ""

  @property
  def slug(self):
    return get_slug(self)

