from src.stack import Stack


def test():
    s = Stack()
    assert s.is_empty() is True

    s.push(4)
    assert s.items == [4]

    s.push("dog")
    assert s.items == [4, "dog"]

    assert s.peek() == "dog"

    s.push(True)
    assert s.items == [4, "dog", True]

    assert s.size() == 3

    assert s.is_empty() is False

    s.push(8.4)
    assert s.items == [4, "dog", True, 8.4]

    assert s.pop() == 8.4

    assert s.pop() is True

    assert s.size() == 2
