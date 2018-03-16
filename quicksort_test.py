import unittest

from quicksort import *

class TestQuickSort(unittest.TestCase):
    def test_partition(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        self.assertEqual(partition(a, 0, len(a) - 1), 3)
