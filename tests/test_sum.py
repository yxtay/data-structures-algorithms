from src.sum import sum_iter, sum_rec


def test_iter():
    numbers = [1, 3, 5, 7, 9]
    assert sum_iter(numbers) == 25


def test_rec():
    numbers = [1, 3, 5, 7, 9]
    assert sum_rec(numbers) == 25
