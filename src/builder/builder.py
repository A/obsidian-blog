import os
import time
from src import fs
from src.blog.blog import Blog
from src.dataclasses.asset_data import AssetData
from src.dataclasses.config_data import ConfigData
from src.obsidian.vault import ObsidianVault
from src.preprocessors.include_header import IncludeHeaderPreprocessor


class Builder:
    """Handles build process"""

    preprocessors = [IncludeHeaderPreprocessor]

    def __init__(self, config: ConfigData, blog: Blog, vault: ObsidianVault):
        self.config = config
        self.blog = blog
        self.vault = vault

    def build(self):
        self.make_build_dir()
        self.copy_assets()
        self.render_all()

    def make_build_dir(self):
        dest_dir = self.config.dest_dir
        print(f'- Prepare a build dir: {dest_dir}')
        fs.rm_dir(dest_dir)
        fs.make_dir(dest_dir)

    def copy_assets(self):
        dest_dir = self.config.dest_dir
        assets_dir = self.config.assets_dir
        public_dir = self.config.public_dir
        assets_dest_dir = self.blog.config.assets_dest_dir
        print(
            f'- Copy assets from {assets_dir} to {dest_dir}/{assets_dest_dir}'
        )
        fs.copy_dir(assets_dir, assets_dest_dir)

    def render_all(self):
        for entity in self.vault.page_types:
            print(f'# Render {entity}:')
            tic = time.perf_counter()

            pages = getattr(self.vault, entity)
            for page in pages:
                print(f'- {page.data.title}')
                self.preprocess_content(page)
                self.process_assets(page)
                if page.data.is_private:
                    print(
                        f"- [SKIP]: '{page.data.title}' is private, add `published: True` attribute to the frontmetter to publish it"
                    )
                    continue
                self.render(page)

            toc = time.perf_counter()

            print('')
            print(
                f'{len(pages)} {entity} have been rendered in {toc-tic:0.4f} seconds\n'
            )

    def render(self, page):
        dest_dir = self.config.dest_dir
        dest = os.path.join(dest_dir, page.data.slug)
        context = self.get_context({'self': page.data})
        html = page.render(context)
        layout = self.get_layout(page)

        if layout is not None:
            html = layout.render(context | {'content': html})

        fs.write_file(dest, html)

    def get_layout(self, node):
        layout_name = node.data.meta.get('layout') or 'main'
        return self.blog.layouts[layout_name]

    def process_assets(self, page):
        for node in page.data.entities:
            entity = node.data
            asset_data = entity.data

            if not issubclass(type(asset_data), AssetData):
                continue

            try:
                dest_dir = self.config.dest_dir
                public_dir = self.config.public_dir
                assets_dest_dir = self.config.assets_dest_dir
                dest_filename = f'{asset_data.id}{asset_data.ext}'

                frm = asset_data.filename
                to = f'{assets_dest_dir}/dest_filename'
                url = os.path.join(public_dir, dest_filename)

                print('URL', url)

                fs.copyfile(frm, to)
                asset_data.filename = url
                print(f'  - [COPY ASSET]: {frm} to {to}')

            except:
                # FIXME: Should skip abs paths and urls
                pass

    def preprocess_content(self, page):
        for node in page.data.entities:
            for processor in self.preprocessors:
                processor.process(node.data)

    def get_context(self, local_ctx):
        global_ctx = {
            'config': {
                'BLOG_TITLE': self.config.blog_title,
                'ASSETS_PATH': self.config.public_dir,
            },
            'layouts': self.blog.layouts,
            'pages': self.vault.pages,
            'posts': self.vault.posts,
        }
        return global_ctx | local_ctx
