import pytest

from src.balance_parenthesis import is_balanced

cases = [
    ("((()))", True),
    ("(()", False),
    ("())", False),
    ("{{([][])}()}", True),
    ("{[])", False),
]


@pytest.mark.parametrize("symbols, expected", cases)
def test_iter(symbols, expected):
    result = is_balanced(symbols)
    assert result == expected
