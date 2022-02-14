from src.dataclasses.content_data import ContentData

# TODO: Fetch link titles?
class FurtherReadingLinksPreprocessor:
    @classmethod
    def process_page(cls, page):
        cls.process_entity(page)

    @classmethod
    def process_entity(cls, entity):
        data: ContentData = entity.data

        if not cls.is_supported_content(data):
            return

        links = data.meta.get('links', None)

        if links is None:
            return

        if type(links) is not list:
            print(
                f'  - [FURTHER READING PREPROCESS] meta links are not valid. Should be a list'
            )

        further_reading_md = '\n**Further Reading**:\n\n'

        for link in links:
            if type(link) is not dict:
                return
            link_name = link.get('name')
            link_url = link.get('url')
            link_md = f'- [{link_name}]({link_url})'
            further_reading_md += f'{link_md}\n'

        data.content = f'{data.content}\n{further_reading_md}'
        print(
            f'  - [PREPROCESS] Rendered further reading section for "{data.title}"'
        )

    @classmethod
    def is_supported_content(cls, data: ContentData):
        if not isinstance(data, ContentData):
            return False

        if data.content == '':
            return False

        return True
