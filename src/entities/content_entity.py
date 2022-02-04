from abc import ABC
from dataclasses import dataclass, field

@dataclass
class ContentEntityData:
  filename: str
  meta: dict = field(default_factory=dict)
  content: str = ""

class ContentEntityInterface(ABC):
  """Basic content entity interface"""
  data: ContentEntityData
