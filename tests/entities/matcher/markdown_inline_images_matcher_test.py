import pytest

from src.entities.matcher.markdown_inline_images_matcher import (
    MarkdownInlineImagesMatcher,
)
from src.entities.matcher.match import Match


@pytest.mark.parametrize(
    'content,expected_result',
    [
        (
            ' ![Title](link.png)',
            Match(
                matcher_id=MarkdownInlineImagesMatcher.matcher_id,
                placeholder='![Title](link.png)',
                url='link.png',
                title='Title',
                ext='.png',
            ),
        )
    ],
)
def test_markdown_inline_images_matcher(content, expected_result):
    [res] = MarkdownInlineImagesMatcher.match(content)
    assert res == expected_result
