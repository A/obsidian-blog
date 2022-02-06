from pybars import Compiler

compiler = Compiler()


def create_template_fn(template_string: str):
    return compiler.compile(template_string)


def render_template(template_string: str, ctx: dict):
    """compile template string to template fn and immediately execute it with a given context"""
    tpl = create_template_fn(template_string)
    return tpl(ctx)
