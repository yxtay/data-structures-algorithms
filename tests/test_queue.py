from src.queue import Queue


def test():
    q = Queue()
    assert q.is_empty() == True

    q.enqueue(4)
    assert q.items == [4]

    q.enqueue("dog")
    assert q.items == ["dog", 4]

    q.enqueue(True)
    assert q.items == [True, "dog", 4]

    assert q.size() == 3

    assert q.is_empty() == False

    q.enqueue(8.4)
    assert q.items == [8.4, True, "dog", 4]

    assert q.dequeue() == 4

    assert q.dequeue() == "dog"

    assert q.size() == 2
