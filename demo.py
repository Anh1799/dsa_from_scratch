from dsa.linked_list import LinkedList
from dsa.stack import Stack
from dsa.queue import Queue
from dsa.hash_table import HashTable
from dsa.bst import BinarySearchTree
from dsa.min_heap import MinHeap

ll = LinkedList()
for x in [1, 2, 3]:
    ll.append(x)
print('Linked list:', ll.to_list(), 'popped:', ll.pop_front())

stack = Stack()
for x in [1, 2, 3]:
    stack.push(x)
print('Stack pop:', stack.pop())

queue = Queue()
for x in [1, 2, 3]:
    queue.enqueue(x)
print('Queue dequeue:', queue.dequeue())

ht = HashTable()
ht.put('cat', 4)
print('Hash table get:', ht.get('cat'))

bst = BinarySearchTree()
for x in [8, 3, 10, 1, 6]:
    bst.insert(x)
print('BST sorted:', bst.inorder())

heap = MinHeap()
for x in [5, 1, 4, 2]:
    heap.push(x)
print('Min heap pop:', [heap.pop() for _ in range(len(heap))])
