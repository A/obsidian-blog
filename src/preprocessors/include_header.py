from src.dataclasses.content_data import ContentData


class IncludeHeaderPreprocessor:
    @staticmethod
    def process_entity(entity):
        data = entity.data
        if not isinstance(data, ContentData):
            return

        if data.content == '':
            return

        header = f"""\

<h2 id="{data.id}" class="subheader">
    <a href="#{data.id}">{data.title}</a>
</h2>

"""
        data.content = f'{header}\n{data.content}'

        print(f'  - [PREPROCESS] Rendered header for "{data.title}"')
