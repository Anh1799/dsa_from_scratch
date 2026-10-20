"""Separate-chaining hash table; Python hash() hashes keys, buckets are lists."""

class HashTable:
    def __init__(self, capacity=8):
        if capacity < 1:
            raise ValueError('capacity must be positive')
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def __len__(self):
        return self._size

    def _index(self, key):
        return hash(key) % len(self._buckets)

    def _resize(self):
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(len(old_buckets) * 2)]
        for bucket in old_buckets:
            for key, value in bucket:
                self._buckets[self._index(key)].append((key, value))

    def put(self, key, value):
        bucket = self._buckets[self._index(key)]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / len(self._buckets) > 0.75:
            self._resize()

    def get(self, key):
        for existing_key, value in self._buckets[self._index(key)]:
            if existing_key == key:
                return value
        raise KeyError(key)

    def remove(self, key):
        bucket = self._buckets[self._index(key)]
        for i, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)
                self._size -= 1
                return value
        raise KeyError(key)

    def contains(self, key):
        return any(existing_key == key for existing_key, _ in self._buckets[self._index(key)])
