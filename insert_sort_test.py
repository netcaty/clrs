import unittest
from random import randrange
from insert_sort import insert_sort, insert_sort_rec

class TestInsertSort(unittest.TestCase):
    '''测试插入排序'''

    def test_insert_sort(self):
        A = [randrange(100) for i in range(10)]
        B = sorted(A, reverse=True)
        insert_sort(A)
        self.assertListEqual(A, B)

    def test_insert_sort_rec(self):
        A = [randrange(100) for i in range(10)]
        B = sorted(A)
        insert_sort_rec(A)
        self.assertListEqual(A, B)
