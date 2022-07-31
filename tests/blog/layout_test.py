import os
import pytest
from src.blog.layout import Layout
from tests.helpers import get_fixture_path


def test_layout_parsing():
    cwd = os.getcwd()
    fixture_path = get_fixture_path("layouts")
    os.chdir(fixture_path)

    layouts = Layout.get_all(fixture_path)

    assert len(layouts.items()) == 3

    os.chdir(cwd)


@pytest.mark.parametrize(
    "layout_name",
    [
        ("index"),
        ("main"),
        ("another"),
    ],
)
def test_layout_rendering(layout_name):
    cwd = os.getcwd()
    fixture_path = get_fixture_path("layouts")
    os.chdir(fixture_path)

    data = "Hello World"
    context = {"data": data}

    layouts = Layout.get_all(fixture_path)
    layout = layouts[layout_name]
    res = layout.render(context)

    assert res == f"<h1>{layout_name}</h1>\n<pre>{data}</pre>\n"

    os.chdir(cwd)
