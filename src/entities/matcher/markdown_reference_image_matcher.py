import os
import re
from src.entities.matcher.abstract_matcher import AbstractMatcher
from src.entities.matcher.match import Match


class MarkdownReferenceImagesMatcher(AbstractMatcher):
    matcher_id = 'MARKDOWN_REFERENCE_IMAGE'

    @classmethod
    def match(cls, content):
        """parse all reference image entities from a given page model"""
        REGEX = r'(\!\[(.*)]\[(.*)\])'

        matches = []
        re_matches = re.findall(REGEX, content)

        for match in re_matches:
            placeholder, title, key = match
            link_re = re.compile('\\[' + key + '\\]:\\s(.*)')
            [url] = re.findall(link_re, content)
            _, ext = os.path.splitext(url)

            match = Match(
                matcher_id=cls.matcher_id,
                placeholder=placeholder,
                url=cls.normalize_path(url),
                title=title,
                ext=ext,
            )
            matches.append(match)
        return matches

    @staticmethod
    def normalize_path(path: str):
        if path[0] == '/':
            return os.path.realpath(path)
        return path
