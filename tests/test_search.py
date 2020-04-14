import pytest

from src.search import binary_search_iter, binary_search_rec, ordered_sequential_search, sequential_search

cases = [
    ([1, 2, 32, 8, 17, 19, 42, 13, 0], 3, -1),
    ([1, 2, 32, 8, 17, 19, 42, 13, 0], 13, 7),
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 3, -1),
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 13, 4),
]


@pytest.mark.parametrize("arr, item, expected", cases)
def test_linear(arr, item, expected):
    result = sequential_search(arr, item)
    assert result == expected


cases = [
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 3, -1),
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 13, 4),
]


@pytest.mark.parametrize("arr, item, expected", cases)
def test_ordered(arr, item, expected):
    result = ordered_sequential_search(arr, item)
    assert result == expected


@pytest.mark.parametrize("arr, item, expected", cases)
def test_binary_rec(arr, item, expected):
    result = binary_search_rec(arr, item)
    assert result == expected


@pytest.mark.parametrize("arr, item, expected", cases)
def test_binary_iter(arr, item, expected):
    result = binary_search_iter(arr, item)
    assert result == expected
