import os
from obsidian_blog import handlebars, fs

class Layout:
  def __init__(self, filename):
    self.filename = filename
    self.name, _ = os.path.splitext(fs.basename(filename))
    with open(filename) as f: hbs_str = f.read()
    self.template_fn = handlebars.create_template_fn(hbs_str)

  def render(self, ctx):
    return self.template_fn(ctx)
