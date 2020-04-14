class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current.value != item and current.next:
            previous, current = current, current.next

        if current.value == item:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next


class OrderedList(UnorderedList):
    def search(self, item):
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            if current.value > item:
                return False
            current = current.next

        return False

    def add(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.value > item:
                break
            previous, current = current, current.next

        temp = Node(item)
        if previous is None:
            temp.next, self.head = self.head, temp
        else:
            temp.next, previous.next = current, temp

    def remove(self, item):
        current = self.head
        previous = None

        while current.value < item and current.next:
            previous, current = current, current.next

        if current.value == item:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
