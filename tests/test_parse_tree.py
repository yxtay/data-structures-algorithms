import pytest

from src.parse_tree import build_parse_tree, construct_expression, evaluate

cases = [
    ("((7+3)*(5-2))", 30),
    ("(3+(4*5))", 23),
]


@pytest.mark.parametrize("expression, expected", cases)
def test(expression, expected):
    parse_tree = build_parse_tree(expression)
    assert evaluate(parse_tree) == expected
    assert construct_expression(parse_tree) == expression
