"""Array-based binary min-heap (no heapq)."""

class MinHeap:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def peek(self):
        if not self._data:
            raise IndexError('peek from empty heap')
        return self._data[0]

    def push(self, value):
        self._data.append(value)
        child = len(self._data) - 1
        while child > 0:
            parent = (child - 1) // 2
            if self._data[parent] <= self._data[child]:
                break
            self._data[parent], self._data[child] = self._data[child], self._data[parent]
            child = parent

    def pop(self):
        if not self._data:
            raise IndexError('pop from empty heap')
        smallest = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            parent = 0
            n = len(self._data)
            while True:
                left = 2 * parent + 1
                right = left + 1
                smallest_index = parent
                if left < n and self._data[left] < self._data[smallest_index]:
                    smallest_index = left
                if right < n and self._data[right] < self._data[smallest_index]:
                    smallest_index = right
                if smallest_index == parent:
                    break
                self._data[parent], self._data[smallest_index] = self._data[smallest_index], self._data[parent]
                parent = smallest_index
        return smallest
