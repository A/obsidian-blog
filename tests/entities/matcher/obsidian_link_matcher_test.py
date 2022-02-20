import pytest

from src.entities.matcher.obsidian_link_matcher import ObsidianLinkMatcher
from src.entities.matcher.match import Match


@pytest.mark.parametrize(
    'content,expected_result',
    [
        (
            ' [[title.png]] ',
            Match(
                matcher_id=ObsidianLinkMatcher.matcher_id,
                placeholder='[[title.png]]',
                url='title.png',
                title=None,
                ext='.png',
            ),
        ),
        (
            ' [[url | title]] ',
            Match(
                matcher_id=ObsidianLinkMatcher.matcher_id,
                placeholder='[[url | title]]',
                url='url',
                title='title',
                ext=None,
            ),
        ),
        (
            ' ![[url | title]] ',
            Match(
                matcher_id=ObsidianLinkMatcher.matcher_id,
                is_embed=True,
                placeholder='![[url | title]]',
                url='url',
                title='title',
                ext=None,
            ),
        ),
    ],
)
def test_markdown_reference_image_matcher(content, expected_result):
    [res] = ObsidianLinkMatcher.match(content)
    assert res == expected_result
