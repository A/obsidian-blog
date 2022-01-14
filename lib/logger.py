from lib.config import VERBOSE

def log(*args):
    if not VERBOSE:
        return None
    print(*args)

