import os
from src.dataclasses.config_data import ConfigData
from tests.helpers import get_fixture_path


def test_config_data_override():
    config = ConfigData()

    config.override({'blog_title': 'abc'})
    assert config.blog_title == 'abc'

    config.override({'blog_title': 'def'})
    assert config.blog_title == 'def'


def test_config_data_dotenv():
    cwd = os.getcwd()
    fixture_path = get_fixture_path('config_data')
    os.chdir(fixture_path)

    config = ConfigData()
    config.load_dotenv()

    assert config.blog_title == 'Dotenv'
    assert config.default_layout == 'dotenv'

    os.chdir(cwd)
