from dataclasses import dataclass
from typing import Optional

@dataclass
class ImageData():
  """Basic image class"""

  filename: str
  placeholder: str
  alt: str
  key: Optional[str] = None
