# Python Data Structures From Scratch

Six implementations with no third-party dependencies. Run from the **project root** using Python 3.10+.

## Start

```bash
python3 demo.py
python3 -m unittest discover -s tests -v
```

## Files

- `dsa/linked_list.py`: singly linked list, head/tail references
- `dsa/stack.py`: LIFO stack using the linked list
- `dsa/queue.py`: FIFO queue using the linked list
- `dsa/hash_table.py`: hash table with separate chaining and resizing
- `dsa/bst.py`: unbalanced binary search tree with unique keys
- `dsa/min_heap.py`: binary min-heap with an array
- `tests/test_structures.py`: unit and edge-case tests
- `demo.py`: usage examples

## Learning path and invariants

1. **LinkedList**: head is the first node; tail is the last node; last node.next is None. `append`, `prepend`, `pop_front` run in O(1), `contains` in O(n).
2. **Stack**: the most recently pushed item is at the head. `push`, `pop`, `peek` O(1).
3. **Queue**: the oldest item is at the head; newest at tail. `enqueue`, `dequeue`, `peek` O(1).
4. **HashTable**: an entry lives in bucket `hash(key) % number_of_buckets`. `put`, `get`, `remove` O(1) expected/amortized, O(n) worst-case; resizing O(n) occasional. Keys must be hashable, and hashes/equality must stay stable while stored.
5. **BinarySearchTree**: left subtree keys are smaller than node key; right subtree keys are larger. `insert`, `contains`, `min` take O(h), with h = tree height; O(log n) if balanced, O(n) if skewed. `inorder` O(n) time and O(h) auxiliary stack space. Duplicate keys are ignored. The recursive traversal can hit Python's recursion limit on very skewed trees.
6. **MinHeap**: each parent <= its children. `push`, `pop` O(log n), `peek` O(1). Underlying storage O(n). Repeated pops yield sorted order.

## Complexity table

| Data structure | Operation | Time | Auxiliary space |
|---|---|---|---|
| Linked list | append/prepend/pop_front | O(1) | O(1) per operation |
| Linked list | contains | O(n) | O(1) |
| Stack | push/pop/peek | O(1) | O(1) per operation |
| Queue | enqueue/dequeue/peek | O(1) | O(1) per operation |
| Hash table | put/get/remove | O(1) expected, O(n) worst | O(1) typical per operation; O(n) on resize |
| BST (unbalanced) | insert/contains/min | O(h) | O(1) for iterative operations |
| BST | inorder | O(n) | O(h) extra + O(n) output |
| Min heap | push/pop | O(log n) | O(1) auxiliary; backing list may resize |
| Min heap | peek | O(1) | O(1) |

Total stored space is O(n) for each structure. `HashTable` uses Python's built-in `hash()` to focus on collision resolution, and lists of key/value pairs as buckets. `MinHeap` intentionally uses a Python list as backing storage, but **does not** use `heapq`. Stack/queue use the project's own linked list.

## Suggested extensions

- Add `remove(value)` and `reverse()` to LinkedList.
- Implement LinkedList indexing (`get(index)`) and analyze its O(n) cost.
- Add `__contains__`, `items()`, and shrinking for HashTable.
- Add `delete(key)` and an **iterative** inorder traversal for BST; later build an AVL tree.
- Add `heapify(iterable)` in O(n) time and compare to repeated insertion O(n log n).
- Add randomized tests comparing behavior against Python `list`, `dict`, and `heapq` as reference implementations.

## Git

From the project directory, after verifying the correct repository and branch:

```bash
git status
git add .
git commit -m "Implement six Python data structures with tests"
git push
```

If the directory was downloaded as a ZIP and isn't linked to your existing repository, clone the existing GitHub repository first and copy these files into the clone rather than forcing a push from an unrelated history.
