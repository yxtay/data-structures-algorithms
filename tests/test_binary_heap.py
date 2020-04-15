from src.binary_heap import BinaryHeap


def test():
    numbers = [9, 6, 5, 2, 3]
    heap = BinaryHeap()
    heap.build_heap(numbers)
    expected = [0, 2, 3, 5, 6, 9]
    assert heap.items == expected
