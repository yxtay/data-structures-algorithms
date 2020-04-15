import pytest

from src.fibonacci import fib_iter, fib_rec

cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
]


@pytest.mark.parametrize("n, expected", cases)
def test_iter(n, expected):
    result = fib_iter(n)
    assert result == expected


@pytest.mark.parametrize("n, expected", cases)
def test_rec(n, expected):
    result = fib_rec(n)
    assert result == expected
