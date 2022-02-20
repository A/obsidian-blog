import os
import re
from .match import Match


class ObsidianMatcher:
    matcher_id = 'OBSIDIAN_BLOG/OBSIDIAN/MATCHER'

    @classmethod
    def match(cls, content):
        REGEXP = r'((?:!)?\[\[([\s\w\d_\-&|\.]*)\]\])'

        matches = []
        re_matches = re.findall(REGEXP, content, flags=re.MULTILINE)

        for re_match in re_matches:
            placeholder, _inner = re_match

            title = None
            url = None
            ext = None
            is_embed = placeholder.startswith('!')
            
            res = _inner.split('|')


            if len(res) >= 1:
                url = res[0].strip()

            if len(res) >= 2:
                title = res[1].strip()


            if url:
                _, ext = os.path.splitext(url)

            match = Match(
                matcher_id=cls.matcher_id,
                is_embed=is_embed,
                placeholder=placeholder,
                url=url,
                title=title,
                ext=ext or None,
            )

            matches.append(match)

        return matches
