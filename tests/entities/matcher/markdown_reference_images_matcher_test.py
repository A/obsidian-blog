import pytest

from src.entities.matcher.markdown_reference_image_matcher import (
    MarkdownReferenceImagesMatcher,
)
from src.entities.matcher.match import Match


@pytest.mark.parametrize(
    'content,expected_result',
    [
        (
            ' ![Title][link]\r\n[link]: link.png',
            Match(
                matcher_id=MarkdownReferenceImagesMatcher.matcher_id,
                placeholder='![Title][link]',
                url='link.png',
                title='Title',
                ext='.png',
            ),
        )
    ],
)
def test_markdown_reference_images_matcher(content, expected_result):
    [res] = MarkdownReferenceImagesMatcher.match(content)
    assert res == expected_result
