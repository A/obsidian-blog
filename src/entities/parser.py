from marko import inline, Markdown


class ObsidianLink(inline.InlineElement):
    pattern = r'\[\[\s*(.+?)\s*(?:\|\s*(.+?)\s*)?]\]'
    parse_children = True

    def __init__(self, match):
        self.placeholder = match.group(0)
        self.target = match.group(1)
        self.title = match.group(2)


class ObsidianEmbed(inline.InlineElement):
    pattern = r'\!\[\[\s*(.+?)\s*(?:\|\s*(.+?)\s*)?]\]'
    parse_children = True

    def __init__(self, match):
        self.placeholder = match.group(0)
        self.target = match.group(1)
        self.title = match.group(2)


class Obsidian:
    elements = [ObsidianEmbed, ObsidianLink]

def markdownFabric(*args, **kwargs):
    markdown = Markdown(*args, **kwargs)
    markdown.use(Obsidian)
    return markdown

def traverse(head, cb):
    key = 'children'

    if not head:
        return

    cb(head)

    if type(head.get(key)) is list:
        for child in head.get(key):
            traverse(child, cb)

def get_all_of_types(element_types, ast): 
    nodes = []
    traverse(ast, lambda n: nodes.append(n))
    return list(
        filter(
            lambda n: n.get('element') in element_types,
            nodes,
        )
    )
