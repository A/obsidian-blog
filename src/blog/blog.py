from src.lib import fs
from src.blog.layout import Layout
from src.dataclasses.config_data import ConfigData


class Blog:
    """Handles blog related setup, like getting layouts, etc"""

    def __init__(self, config: ConfigData):
        self.config = config
        self.layouts = self.load_layouts()

    def load_layouts(self):
        return Layout.get_all(self.config.layouts_dir)
