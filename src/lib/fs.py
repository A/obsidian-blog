import frontmatter
import glob
import os
import shutil
from distutils.dir_util import copy_tree
from shutil import copyfile


def change_ext(ext: str, file_path: str):
    """Changes extension in path"""
    pre, _ = os.path.splitext(file_path)
    return pre + '.' + ext


def rm_dir(directory: str):
    """Removes a given dir if exists"""
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)


def make_dir(directory: str):
    """creates a directory"""
    try:
        os.mkdir(directory)
    except:
        pass


def copy_dir(source: str, dest: str):
    """copies given directory content into another one"""
    copy_tree(source, dest)


def get_files_in_dir(dir: str, filter_partials=False):
    """returns files from given dir with optional partials filtering"""
    file_names = [
        f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))
    ]

    if filter_partials:
        file_names = filter(
            lambda f: not f.startswith('_', 0, -1),
            file_names,
        )

    return file_names


def basename(path: str):
    """returns a file basename"""
    return os.path.basename(path)


def copy_file(src: str, dest: str):
    copyfile(src, dest)


def write_file(dest, content):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'a') as f:
        print(content, file=f)


def find_one_by_glob(g):
    filenames = glob.glob(g, recursive=True)
    return filenames[0]


def load(filename):
    try:
        f = frontmatter.load(filename)
        return [filename, f.metadata, f.content]
    except Exception as error:
        print(f'[ERROR] There is an error loading {filename}: {error}')
        exit(1)


def normalize_path(path: str):
    if path[0] == '/':
        return os.path.realpath(path)
    return path
