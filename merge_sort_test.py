import unittest
from random import randrange

from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    '''测试归并排序'''

    def test_insert_sort(self):
        A = [randrange(100) for i in range(10)]
        B = sorted(A)
        merge_sort(A)
        self.assertListEqual(A, B)

    def test_insert_sort2(self):
        A = [randrange(100) for i in range(100)]
        B = sorted(A)
        merge_sort(A)
        self.assertListEqual(A, B)
