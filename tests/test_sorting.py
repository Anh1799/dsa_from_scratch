
import unittest

from algorithms.sorting import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort
)


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.algorithms = [
            bubble_sort,
            selection_sort,
            insertion_sort,
            merge_sort,
            quick_sort,
            heap_sort
        ]

    def test_unsorted(self):
        for sort in self.algorithms:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(
                    sort([5, 2, 8, 1, 3]),
                    [1, 2, 3, 5, 8]
                )

    def test_empty(self):
        for sort in self.algorithms:
            self.assertEqual(sort([]), [])

    def test_duplicates(self):
        for sort in self.algorithms:
            self.assertEqual(
                sort([4, 2, 4, 1]),
                [1, 2, 4, 4]
            )

    def test_negative_numbers(self):
        for sort in self.algorithms:
            self.assertEqual(
                sort([-3, 5, 0, -1]),
                [-3, -1, 0, 5]
            )

    def test_original_unchanged(self):
        nums = [3, 1, 2]

        for sort in self.algorithms:
            sort(nums)
            self.assertEqual(nums, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
