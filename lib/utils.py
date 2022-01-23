import frontmatter


def is_private(entity):
  return bool(entity.meta.private)

def read_file(path):
  return frontmatter.load(path)
