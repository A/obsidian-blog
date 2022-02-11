from src.dataclasses.content_data import ContentData


class IncludeHeaderPreprocessor:
    @staticmethod
    def process(entity):
        data = entity.data
        if not isinstance(data, ContentData):
            return

        if data.content == '':
            return

        header = f'<h2 id="{data.id}">{data.title}</h2>'
        data.content = f'{header}\n{data.content}'

        print(f'  - [PREPROCESS] Rendered header for "{data.title}"')
