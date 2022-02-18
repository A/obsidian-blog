from typing import Optional
from dataclasses import dataclass


@dataclass
class Match:
    matcher_id: str
    placeholder: Optional[str] = None
    url: Optional[str] = None
    title: Optional[str] = None
    ext: Optional[str] = None
