from src.dataclasses.content_data import ContentData
from src.preprocessors.further_reading import FurtherReadingLinksPreprocessor
from tests.helpers import DummyInclude


def test_further_reading_preprocessor(snapshot):
    content_data = ContentData(
        filename='a.md',
        meta={
            'links': [
                {'name': 'name.a', 'url': 'url.a'},
                {'name': 'name.b', 'url': 'url.b'},
                {'name': 'name.c', 'url': 'url.c'},
            ]
        },
        content='content',
    )
    entity = DummyInclude(content_data)

    FurtherReadingLinksPreprocessor.process_entity(entity)

    entity.data.content

    snapshot.assert_match(content_data.content, f'further_reading_test.html')
