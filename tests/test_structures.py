import unittest
from dsa.linked_list import LinkedList
from dsa.stack import Stack
from dsa.queue import Queue
from dsa.hash_table import HashTable
from dsa.bst import BinarySearchTree
from dsa.min_heap import MinHeap


class TestLinkedList(unittest.TestCase):
    def test_append_prepend_and_iteration(self):
        a = LinkedList()
        a.append(2)
        a.prepend(1)
        a.append(3)
        self.assertEqual(a.to_list(), [1, 2, 3])
        self.assertEqual(len(a), 3)
        self.assertTrue(a.contains(2))
        self.assertFalse(a.contains(4))

    def test_remove_and_reuse(self):
        a = LinkedList()
        with self.assertRaises(IndexError):
            a.pop_front()
        a.append(4)
        self.assertEqual(a.pop_front(), 4)
        self.assertTrue(a.is_empty())
        a.append(5)
        self.assertEqual(a.to_list(), [5])


class TestStack(unittest.TestCase):
    def test_lifo(self):
        s = Stack()
        s.push('a')
        s.push('b')
        self.assertEqual(s.peek(), 'b')
        self.assertEqual(s.pop(), 'b')
        self.assertEqual(s.pop(), 'a')
        self.assertTrue(s.is_empty())
        with self.assertRaises(IndexError):
            s.peek()


class TestQueue(unittest.TestCase):
    def test_fifo(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        self.assertEqual(q.peek(), 'a')
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(q.dequeue(), 'b')
        with self.assertRaises(IndexError):
            q.dequeue()
        q.enqueue('c')
        self.assertEqual(q.dequeue(), 'c')


class CollidingKey:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 42

    def __eq__(self, other):
        return isinstance(other, CollidingKey) and self.value == other.value


class TestHashTable(unittest.TestCase):
    def test_get_update_remove_and_resize(self):
        h = HashTable(2)
        for i in range(30):
            h.put(i, i * 10)
        self.assertEqual(len(h), 30)
        h.put(3, 999)
        self.assertEqual(len(h), 30)
        self.assertEqual(h.get(3), 999)
        self.assertEqual(h.remove(3), 999)
        self.assertFalse(h.contains(3))
        with self.assertRaises(KeyError):
            h.get(3)

    def test_collisions(self):
        h = HashTable()
        a, b = CollidingKey('a'), CollidingKey('b')
        h.put(a, 1)
        h.put(b, 2)
        self.assertEqual(h.get(a), 1)
        self.assertEqual(h.get(b), 2)
        self.assertEqual(h.remove(a), 1)
        self.assertEqual(h.get(b), 2)


class TestBST(unittest.TestCase):
    def test_inorder_and_find(self):
        tree = BinarySearchTree()
        for key in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            self.assertTrue(tree.insert(key))
        self.assertFalse(tree.insert(6))
        self.assertEqual(len(tree), 9)
        self.assertEqual(tree.inorder(), [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertTrue(tree.contains(7))
        self.assertFalse(tree.contains(12))
        self.assertEqual(tree.min(), 1)

    def test_empty(self):
        with self.assertRaises(IndexError):
            BinarySearchTree().min()


class TestHeap(unittest.TestCase):
    def test_sorted_pop_with_duplicates(self):
        h = MinHeap()
        with self.assertRaises(IndexError):
            h.pop()
        for n in [8, 3, 5, 1, 3, 9, -2]:
            h.push(n)
        self.assertEqual(h.peek(), -2)
        self.assertEqual([h.pop() for _ in range(7)], [-2, 1, 3, 3, 5, 8, 9])
        self.assertEqual(len(h), 0)


if __name__ == '__main__':
    unittest.main()
