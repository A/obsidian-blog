# import mistletoe
# from mistletoe import Document
# from mistletoe.ast_renderer import ASTRenderer
# import src.markdown.markdown
import json
from src.markdown.markdown import markdown



def test_marko():
    content = """\
![[Hello]]
![[Hello | World]]
[[Hello]]
[[Hello | World]]
[[One | Two]] [[Three | Four]]\
"""

    ast = markdown.parse(content)
    html = markdown.render(ast)
    print(html)
    # res = HTMLRenderer.render_children(res)
    # print(res)
    assert True == False
