import pytest

from src.palindrome import is_palindrome

cases = [
    ("lsdkjfskf", False),
    ("radar", True),
]


@pytest.mark.parametrize("characters, expected", cases)
def test(characters, expected):
    result = is_palindrome(characters)
    assert result == expected
