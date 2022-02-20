from typing import Optional
from dataclasses import dataclass


@dataclass
class Match:
    matcher_id: str
    is_embed: bool = False
    placeholder: Optional[str] = None
    url: Optional[str] = None
    title: Optional[str] = None
    ext: Optional[str] = None
