import os
import re

from .abstract_matcher import AbstractMatcher
from .match import Match


class MarkdownInlineImageMatcher(AbstractMatcher):
    matcher_id = 'OBSIDIAN_BLOG/MARKDOWN/INLINE_IMAGE/Mather'

    @classmethod
    def match(cls, content: str):
        REGEX = r'(\!\[(.*)\]\((.*)\))'

        matches = []
        re_matches = re.findall(REGEX, content)

        for match in re_matches:
            placeholder, title, url = match
            _, ext = os.path.splitext(url)
            match = Match(
                matcher_id=cls.matcher_id,
                placeholder=placeholder,
                url=url,
                title=title,
                ext=ext,
            )
            matches.append(match)

        return matches
