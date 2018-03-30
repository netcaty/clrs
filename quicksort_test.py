import unittest

from quicksort import *

class TestQuickSort(unittest.TestCase):
    def test_partition(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        self.assertEqual(partition(a, 0, len(a) - 1), 3)

    def test_quicksort(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        quicksort(a)
        self.assertEqual(a, [1, 2, 3, 4 ,5, 6, 7, 8])
