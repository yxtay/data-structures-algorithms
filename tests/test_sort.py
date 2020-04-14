import pytest

from src.sort import (
    bubble_sort, bucket_sort, counting_sort, heap_sort, insertion_sort, merge_sort, quick_sort, radix_sort,
    selection_sort, shell_sort,
)

cases = [
    ([1], [1]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 3, 2], [1, 2, 3]),
    ([2, 1, 3], [1, 2, 3]),
    ([2, 3, 1], [1, 2, 3]),
    ([3, 1, 2], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([23, 1, 45, 34, 7], [1, 7, 23, 34, 45]),
    ([45, 34, 23, 7, 1], [1, 7, 23, 34, 45]),
    ([3, 6, 1, 8], [1, 3, 6, 8]),
    ([24, 56, 1, 50, 17], [1, 17, 24, 50, 56]),
    ([34, 23, 1, 67, 4], [1, 4, 23, 34, 67]),
    ([23, 12, 1, 17, 45, 2, 13], [1, 2, 12, 13, 17, 23, 45]),
    ([6, 5, 12, 10, 9, 1], [1, 5, 6, 9, 10, 12]),
    ([9, 5, 1, 4, 3], [1, 3, 4, 5, 9]),
    ([8, 7, 2, 1, 0, 9, 6], [0, 1, 2, 6, 7, 8, 9]),
    ([12, 11, 13, 5, 6, 7], [5, 6, 7, 11, 12, 13]),
]


@pytest.mark.parametrize("arr, expected", cases)
def test_bubble_sort(arr, expected):
    bubble_sort(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_selection_sort(arr, expected):
    selection_sort(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_merge_sort(arr, expected):
    merge_sort(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_insertion_sort(arr, expected):
    insertion_sort(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_quick_sort(arr, expected):
    quick_sort(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_heap_sort(arr, expected):
    heap_sort(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_counting_sort(arr, expected):
    counting_sort(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_radix_sort(arr, expected):
    radix_sort(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", cases)
def test_shell_sort(arr, expected):
    shell_sort(arr)
    assert arr == expected


def test_bucket_sort():
    arr = [.42, .32, .33, .52, .37, .47, .51]
    bucket_sort(arr)
    expected = [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
    assert arr == expected
