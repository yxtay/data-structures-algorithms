import pytest

from src.postfix import evaluate_postfix, to_postfix

cases = [
    ("A * B + C * D", "A B * C D * +"),
    ("( A + B ) * C - ( D - E ) * ( F + G )", "A B + C * D E - F G + * -"),
    ("( A + B ) * ( C + D )", "A B + C D + *"),
    ("( A + B ) * C", "A B + C *"),
    ("A + B * C", "A B C * +"),
    ("( 7 + 8 ) / ( 3 + 2 )", "7 8 + 3 2 + /"),
]


@pytest.mark.parametrize("infix, expected", cases)
def test_to_postfix(infix, expected):
    result = to_postfix(infix)
    assert result == expected


def test_evaluate():
    expression = "7 8 + 3 2 + /"
    assert evaluate_postfix(expression) == 3.0
