import pytest

from src.entities.matcher.markdown_inline_image_matcher import (
    MarkdownInlineImageMatcher,
)
from src.entities.matcher.match import Match


@pytest.mark.parametrize(
    'content,expected_result',
    [
        (
            ' ![Title](link.png)',
            Match(
                matcher_id=MarkdownInlineImageMatcher.matcher_id,
                placeholder='![Title](link.png)',
                url='link.png',
                title='Title',
                ext='.png',
            ),
        )
    ],
)
def test_markdown_inline_image_matcher(content, expected_result):
    [res] = MarkdownInlineImageMatcher.match(content)
    assert res == expected_result
