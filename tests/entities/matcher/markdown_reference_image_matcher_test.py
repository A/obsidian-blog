import pytest

from src.entities.matcher.markdown_reference_image_matcher import (
    MarkdownReferenceImageMatcher,
)
from src.entities.matcher.match import Match


@pytest.mark.parametrize(
    'content,expected_result',
    [
        (
            ' ![title][reference]\n[reference]: image.png',
            Match(
                matcher_id=MarkdownReferenceImageMatcher.matcher_id,
                placeholder='![title][reference]',
                url='image.png',
                title='title',
                ext='.png',
            ),
        )
    ],
)
def test_markdown_reference_image_matcher(content, expected_result):
    [res] = MarkdownReferenceImageMatcher.match(content)
    assert res == expected_result
