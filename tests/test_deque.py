from src.deque import Deque


def test():
    d = Deque()
    assert d.is_empty() is True

    d.add_rear(4)
    assert d.items == [4]

    d.add_rear("dog")
    assert d.items == ["dog", 4]

    d.add_front("cat")
    assert d.items == ["dog", 4, "cat"]

    d.add_front(True)
    assert d.items == ["dog", 4, "cat", True]

    assert d.size() == 4

    assert d.is_empty() is False

    d.add_rear(8.4)
    assert d.items == [8.4, "dog", 4, "cat", True]

    assert d.remove_rear() == 8.4

    assert d.remove_front() is True
