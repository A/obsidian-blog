from dataclasses import dataclass, fields
from dotenv.main import dotenv_values


@dataclass
class ConfigData:
    drafts: bool = False
    blog_title: str = 'My Blog'
    dest_dir: str = '.build'
    source_dir: str = '.blog'
    posts_dir: str = 'Posts'
    pages_dir: str = 'Pages'
    layouts_dir: str = '.blog/_layouts'
    assets_dir: str = '.blog/_assets'
    assets_dest_dir: str = '.build/static'
    public_dir: str = '/static'
    default_layout: str = 'main'
    port: int = 4200

    def override(self, config: dict):
        """override config values from a given dict"""
        for i in fields(ConfigData):
            if i.name in config:
                setattr(self, i.name, config[i.name])

    def load_dotenv(self):
        self.override(dotenv_values('.env'))


config = ConfigData()
