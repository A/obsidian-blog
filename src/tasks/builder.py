import time
from src.dataclasses.config_data import ConfigData
from src.obsidian.vault import ObsidianVault
from src.blog.blog import Blog
from src.builder.builder import Builder

lock = False


class BuilderTask:
    @staticmethod
    def run(config=ConfigData):
        global lock
        if lock:
            return

        lock = True
        tic = time.perf_counter()
        vault = ObsidianVault(config=config)
        blog = Blog(config=config)
        builder = Builder(config=config, vault=vault, blog=blog)
        builder.build()
        toc = time.perf_counter()

        print('---\n')
        print(f'The build has been finished in {toc - tic:0.4f} seconds\n')
        lock = False
