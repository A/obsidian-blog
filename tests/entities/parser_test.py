from src.entities.parser import markdownFabric, traverse
from marko.ast_renderer import ASTRenderer


def test_entities_parser():
    content = """\
`[[Negative]]`
`![[Negative]]`
![[Hello]]
![[Hello | World]]
[[Hello]]
[[Hello | World]]
[[One | Two]] [[Three | Four]]\
"""

    markdown = markdownFabric(renderer=ASTRenderer)
    ast = markdown(content)

    nodes = []
    traverse(ast, lambda n: nodes.append(n))
    nodes = list(
        filter(
            lambda n: n.get("element") in ["obsidian_link", "obsidian_embed"],
            nodes,
        )
    )

    node = nodes[0]
    assert node["placeholder"] == "![[Hello]]"
    assert node["title"] == None
    assert node["target"] == "Hello"
    assert node["element"] == "obsidian_embed"

    node = nodes[1]
    assert node["placeholder"] == "![[Hello | World]]"
    assert node["title"] == "World"
    assert node["target"] == "Hello"
    assert node["element"] == "obsidian_embed"

    node = nodes[2]
    assert node["placeholder"] == "[[Hello]]"
    assert node["title"] == None
    assert node["target"] == "Hello"
    assert node["element"] == "obsidian_link"

    node = nodes[3]
    assert node["placeholder"] == "[[Hello | World]]"
    assert node["title"] == "World"
    assert node["target"] == "Hello"
    assert node["element"] == "obsidian_link"

    node = nodes[4]
    assert node["placeholder"] == "[[One | Two]]"
    assert node["title"] == "Two"
    assert node["target"] == "One"
    assert node["element"] == "obsidian_link"

    node = nodes[5]
    assert node["placeholder"] == "[[Three | Four]]"
    assert node["title"] == "Four"
    assert node["target"] == "Three"
    assert node["element"] == "obsidian_link"
