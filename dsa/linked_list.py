"""Singly linked list with explicit nodes."""

class _Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def prepend(self, value):
        self.head = _Node(value, self.head)
        if self.tail is None:
            self.tail = self.head
        self._size += 1

    def append(self, value):
        node = _Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self._size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError('pop from empty linked list')
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        if self.head is None:
            self.tail = None
        return value

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def to_list(self):
        return list(self)
