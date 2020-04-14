class Queue(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        raise ValueError("items cannot be set.")

    @items.deleter
    def items(self):
        raise ValueError("items cannot be deleted.")
