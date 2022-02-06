from src.dataclasses.config_data import ConfigData
from src.obsidian.page import Page


class ObsidianVault:
    """ObsidianVault handles posts and pages look up"""

    page_types = ['pages', 'posts']

    def __init__(self, config: ConfigData):
        self.config = config
        self.posts = self.load_posts()
        self.pages = self.load_pages()

    def load_posts(self):
        return Page.get_all(self.config.posts_dir)

    def load_pages(self):
        return Page.get_all(self.config.pages_dir)
