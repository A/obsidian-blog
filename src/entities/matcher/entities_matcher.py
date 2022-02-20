from enum import Enum

from .markdown_inline_images_matcher import MarkdownInlineImageMatcher


class Target(Enum):
    MARKDOWN_INLINE_IMAGE = 'MARKDOWN_INLINE_IMAGE'
    MARKDOWN_REFERENCE_IMAGE = 'MARKDOWN_REFERENCE_IMAGE'
    OBSIDIAN_EMBED = 'OBSIDIAN_EMBED'
    OBSIDIAN_LINK = 'OBSIDIAN_LINK'


class Category(Enum):
    EMBED = 'EMBED'
    LINK = 'LINK'


class EntitiesMatcher:
    matchers = [
        MarkdownInlineImageMatcher,
    ]

    @classmethod
    def get_matches(cls, content: str):
        return [
            match
            for matcher in cls.matchers
            for match in matcher.match(content)
        ]

    @classmethod
    def match_all(cls, content: str):
        return [
            *cls.get_obsidian_embed(content),
            *cls.get_obsidian_link(content),
        ]

    @classmethod
    def get_obsidian_embed(cls, content: str):
        MW_IMG_REGEXP = r'(\!\[\[(.*)\]\])'
        MW_INCLUDE_REGEXP = r'^(\[\[([\s\w\d_\-&|]*)\]\])$'
        return []

    @classmethod
    def get_obsidian_link(cls, content: str):
        MATCHERS = [
            r'^(\[\[([\s\w\d_\-&|]*)\]\])(?:.+)$',
            r'(?!^)(\[\[([\s\w\d_\-&|]*)\]\])',
        ]
        return []
