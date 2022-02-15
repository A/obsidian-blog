from src.dataclasses.content_data import ContentData
from src.preprocessors.include_header import IncludeHeaderPreprocessor
from tests.helpers import DummyInclude


def test_include_header_preprocessor(snapshot):
    content_data = ContentData(
        filename='a.md',
        meta={'title': 'abc'},
        content='content',
    )

    entity = DummyInclude(content_data)
    IncludeHeaderPreprocessor.process_entity(entity)

    entity.data.content

    snapshot.assert_match(content_data.content, f'include_header_test.html')
