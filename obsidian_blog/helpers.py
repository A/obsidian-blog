import os

# TODO: URLs
def normalize_path(path: str):
  if path[0] == '/':
    return os.path.realpath(path)
  return path
