"""FIFO queue backed by our linked list with a tail pointer."""
from .linked_list import LinkedList


class Queue:
    def __init__(self):
        self._items = LinkedList()

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        return self._items.pop_front()

    def peek(self):
        if self._items.head is None:
            raise IndexError('peek from empty queue')
        return self._items.head.value

    def is_empty(self):
        return self._items.is_empty()

    def __len__(self):
        return len(self._items)
