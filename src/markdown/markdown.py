from marko import inline, Markdown, ast_renderer, html_renderer


class ObsidianLink(inline.InlineElement):
    pattern = r'\[\[\s*(.+?)\s*(?:\|\s*(.+?)\s*)?]\]'
    parse_children = True

    def __init__(self, match):
        self.target = match.group(1)
        self.title = match.group(2)
        self.document = None


class ObsidianEmbed(inline.InlineElement):
    pattern = r'\!\[\[\s*(.+?)\s*(?:\|\s*(.+?)\s*)?]\]'
    parse_children = True

    def __init__(self, match):
        self.target = match.group(1)
        self.title = match.group(2)
        self.document = None


class Obsidian:
    elements = [ObsidianEmbed, ObsidianLink]


markdown = Markdown()
markdown.use(Obsidian)

# HTMLRenderer = html_renderer.HTMLRenderer()
