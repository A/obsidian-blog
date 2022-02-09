from dataclasses import dataclass
import os
from src.lib import fs
from src.converters import handlebars


@dataclass
class Layout:
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f:
            hbs_str = f.read()
        self.template_fn = handlebars.create_template_fn(hbs_str)

    @property
    def name(self):
        name, _ = os.path.splitext(os.path.basename(self.filename))
        return name

    @property
    def fn(self):
        with open(self.filename) as f:
            hbs_str = f.read()
        return handlebars.create_template_fn(hbs_str)

    @staticmethod
    def get_all(layouts_dir):
        layouts = {}

        for file in fs.get_files_in_dir(layouts_dir):
            path = os.path.join(layouts_dir, file)
            layout = Layout(path)
            layouts[layout.name] = layout

        return layouts

    def render(self, ctx):
        return self.fn(ctx)
