"""Unbalanced binary search tree; unique comparable keys."""

class _Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    def insert(self, key):
        if self.root is None:
            self.root = _Node(key)
            self._size += 1
            return True
        node = self.root
        while True:
            if key == node.key:
                return False  # duplicates are ignored
            if key < node.key:
                if node.left is None:
                    node.left = _Node(key)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = _Node(key)
                    break
                node = node.right
        self._size += 1
        return True

    def contains(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self):
        def visit(node):
            if node is not None:
                yield from visit(node.left)
                yield node.key
                yield from visit(node.right)
        return list(visit(self.root))

    def min(self):
        if self.root is None:
            raise IndexError('min from empty BST')
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key
