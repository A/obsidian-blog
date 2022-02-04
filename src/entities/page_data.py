from dataclasses import dataclass, field

@dataclass
class PageData:
  filename: str
  content: str
  meta: dict = field(default_factory=dict)
  entities: list = field(default_factory=list)

