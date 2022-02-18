import os
import re
from src.dataclasses.content_data import ContentData
from src.lib import fs


class ObsidianLinkMatcher:
    matcher_id = 'OBSIDIAN_LINK_MATCHER'

    @classmethod
    def match(cls, content):
        # TODO: move body into subregex
        REGEXP = r'(\[\[([\s\w\d_\-&|]*)\]\])'

        matches = []
        re_matches = re.findall(REGEXP, content, flags=re.MULTILINE)

        for re_match in re_matches:
            placeholder, title = re_match
            try:
                filename = fs.find_one_by_glob(f'**/{title}.md')
                _, ext = os.path.splitext(title)

                if not ext:
                    ext = '.md'

                re_match = Match(
                    matcher_id=cls.matcher_id,
                    placeholder=placeholder,
                    url=cls.normalize_path(url),
                    title=title,
                    ext=ext,
                )

                matches.append(include)
                print(f'- [PARSED]: Include: {placeholder}')
            except Exception as e:
                print(f'- [NOT FOUND] "{placeholder}" {e}')

        return matches
