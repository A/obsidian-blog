import markdown

md_parser = markdown.Markdown(
    extensions = [
        'fenced_code',
        'markdown_link_attr_modifier',
        'attr_list',
    ],
    extension_configs = {
        'markdown_link_attr_modifier': {
            'new_tab': 'on',
            'no_referrer': 'external_only',
            'auto_title': 'on',
        },
    }
)

def parse_markdown(md_str: str):
  return md_parser.convert(md_str)
