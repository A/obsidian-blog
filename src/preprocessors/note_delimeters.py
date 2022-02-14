from src.dataclasses.content_data import ContentData


class NoteDelimeterPreprocessor:
    @staticmethod
    def process_entity(entity):
        data = entity.data
        if not isinstance(data, ContentData):
            return

        if data.content == '':
            return

        delimeter = '---'

        data.content = f'{data.content}\n\n{delimeter}\n'

        print(f'  - [PREPROCESS] Rendered delimeter for "{data.title}"')
