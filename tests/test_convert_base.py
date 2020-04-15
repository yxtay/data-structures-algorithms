import pytest

from src.convert_base import convert_base_rec, convert_base_stack

cases = [
    (25, 2, "11001"),
    (25, 16, "19"),
    (1453, 16, "5ad"),
]


@pytest.mark.parametrize("number, base, expected", cases)
def test_stack(number, base, expected):
    result = convert_base_stack(number, base)
    assert result == expected


@pytest.mark.parametrize("number, base, expected", cases)
def test_rec(number, base, expected):
    result = convert_base_rec(number, base)
    assert result == expected
