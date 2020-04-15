import pytest

from src.lattice_paths import num_paths_dp, num_paths_dp_2, num_paths_rec

cases = [(2, 1, 3), (1, 2, 3), (2, 2, 6), (10, 10, 184756)]


@pytest.mark.parametrize("height, width, expected", cases)
def test_rec(height, width, expected):
    result = num_paths_rec(height, width)
    assert result == expected


@pytest.mark.parametrize("height, width, expected", cases)
def test_dp(height, width, expected):
    result = num_paths_dp(height, width)
    assert result == expected


@pytest.mark.parametrize("height, width, expected", cases)
def test_dp(height, width, expected):
    result = num_paths_dp_2(height, width)
    assert result == expected
