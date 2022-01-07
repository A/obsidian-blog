import os
import re
import glob
import markdown
import pybars

from lib.helpers import change_ext, build_slug

#
# Bunch of helpers to make a blog from obsidian notes
#

INCLUDE_REGEXP = r'\[\[(.*)\]\]'

pybars_compiler = pybars.Compiler()


def make_dest_dir(dest_dir: str):
    """Purge old build artefacts and make an empty destination dir"""

    if os.path.exists(dest_dir) and os.path.isdir(dest_dir):
        print('Clear previous build')
        shutil.rmtree(dest_dir)

    os.mkdir(dest_dir)


def get_posts(source_dir: str):
    """Returns all posts in the given directory"""
    file_names = [
        f for f in os.listdir(source_dir)
        if os.path.isfile(os.path.join(source_dir, f))
    ]

    file_names = filter(
        lambda f: not f.startswith('_', 0, -1),
        file_names,
    )

    posts = []

    for file_name in file_names:
        post = {}
        post['file'] = os.path.join(source_dir, file_name)

        with open(post['file']) as f: md_content = f.read()

        md_content = unwrap_includes(md_content)
        md_parser = markdown.Markdown(
            extensions = ['meta', 'fenced_code', 'markdown_link_attr_modifier'],
            extension_configs = {
                'markdown_link_attr_modifier': {
                    'new_tab': 'on',
                    'no_referrer': 'external_only',
                    'auto_title': 'on',
                },
            }
        )

        post['html'] = md_parser.convert(md_content)
        post['meta'] = md_parser.Meta
        post['slug'] = build_slug(post['file'])
        
        posts.append(post)



    return sorted(
        posts,
        key=lambda post: post['meta']['date'],
        reverse=True
    )

def get_pages(pages_dir: str):
    """returns all hbs pages in the given dir"""
    pages = []

    file_names = [
        f for f in os.listdir(pages_dir)
        if os.path.isfile(os.path.join(pages_dir, f))
    ]

    for file_name in file_names:
        page = {}
        page['name'] = re.sub(r'\.hbs$', '', file_name)
        page['file'] = os.path.join(pages_dir, file_name)
        page['slug'] = build_slug(page['name'])

        with open(page['file']) as f: raw = f.read()
        page['raw_content'] = raw

        pages.append(page)
    
    return pages


def get_all_includes(content: str):
    """Returns a list of all obsidian includes"""

    matches = re.findall(INCLUDE_REGEXP, content)
    return list(filter(
        lambda include: include is not None,
        map(get_include, matches)
    ))


def get_include(name: str):
    """Returns a parsed include meta and content"""

    matches = glob.glob('**/' + name + '.md', recursive=True)
    file = matches[0] if len(matches) > 0 else None

    if file == None: return None

    with open(file) as f: content = f.read()

    return {
        'name': name,
        'file': file,
        'content':  content
    }

def unwrap_includes(content: str):
    result = content

    for include in get_all_includes(result):
        name = include['name']
        file = include['file']
        content = include['content']

        placeholder = '[[' + name + ']]'

        result = result.replace(placeholder, content)

    return result

def get_layouts(layouts_dir: str):
    """return dict by name of all hbs layouts from a given dir"""
    layouts = {}

    for file_name in os.listdir(layouts_dir):
        rel_path = os.path.join(layouts_dir, file_name)
        name, _ = os.path.splitext(file_name)

        with open(rel_path) as f: raw = f.read()

        layouts[name] = pybars_compiler.compile(raw)

    return layouts

def render(hbs_str: str, ctx: dict):
    template = pybars_compiler.compile(hbs_str)
    return template(ctx)

