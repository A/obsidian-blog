import os
from src.dataclasses.config_data import ConfigData


class PreflightCheckTask:
    @classmethod
    def run(cls, config=ConfigData):
        directories = (
            config.pages_dir,
            config.posts_dir,
            config.dest_dir,
            config.layouts_dir,
            config.assets_dir,
        )
        for d in directories:
            cls.validate_directory_exists(d)

    @classmethod
    def validate_directory_exists(cls, directory):
        if not os.path.isdir(directory):

            raise Exception(
                f'Directory {directory} not found. Are you in a properly configured vault?'
            )
