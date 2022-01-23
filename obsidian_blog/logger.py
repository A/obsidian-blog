from obsidian_blog.config import VERBOSE

def log(*args):
    if not VERBOSE:
        return None
    print(*args)

