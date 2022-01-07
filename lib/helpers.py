import os
import shutil
from slugify import slugify
from distutils.dir_util import copy_tree

def change_ext(ext: str, file_path: str):
    """Changes extension in path"""

    pre, _ = os.path.splitext(file_path)
    return pre + '.' + ext

def build_slug(file_path: str):
    url = change_ext('', file_path)
    return slugify(url) + '.html'

def rm_dir(directory: str):
    """Removes a given dir if exists"""
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)

def make_dir(directory: str):
    """creates a directory"""
    os.mkdir(directory)

def copy_dir(source: str, dest: str):
    """copies given directory content into another one"""
    copy_tree(source, dest)
