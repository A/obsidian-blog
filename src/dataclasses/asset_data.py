from dataclasses import dataclass
import os
from typing import Optional
from slugify.slugify import slugify


@dataclass
class AssetData:
    """Basic image class"""

    filename: str = ''
    placeholder: str = ''
    alt: str = ''
    key: Optional[str] = None

    @property
    def id(self):
        filename, _ = os.path.splitext(self.filename)
        return slugify(filename)

    @property
    def ext(self):
        _, ext = os.path.splitext(self.filename)
        return ext
