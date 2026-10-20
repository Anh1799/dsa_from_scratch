"""Stack backed by our linked list."""
from .linked_list import LinkedList


class Stack:
    def __init__(self):
        self._items = LinkedList()

    def push(self, value):
        self._items.prepend(value)

    def pop(self):
        return self._items.pop_front()

    def peek(self):
        if self._items.head is None:
            raise IndexError('peek from empty stack')
        return self._items.head.value

    def is_empty(self):
        return self._items.is_empty()

    def __len__(self):
        return len(self._items)
