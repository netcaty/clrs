import unittest

from heap import max_heap, heapsort


class TestHeap(unittest.TestCase):
    def test_build_max_heap(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        h = max_heap(a)
        self.assertEqual(h, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_heapsort(self):
        a = [4, 1, 3, 3, 16, 9, 10, 14, 8, 7]
        heapsort(a)
        self.assertEqual(a, [1, 3, 3, 4, 7, 8, 9, 10, 14, 16])

    def test_str(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        h = max_heap(a)
        self.assertEqual(str(h), '[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]')

    def test_extract_maximum(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        b = [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
        h = max_heap(a)
        for i, v in enumerate(b):
            self.assertEqual(h.heap_extract_maximum(), v)
        with self.assertRaises(BufferError):
            h.heap_extract_maximum()

    def test_heap_insert(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        h = max_heap([])
        h.heap_insert(4)
        self.assertEqual(h, [4])
        h.heap_insert(1)
        self.assertEqual(h, [4, 1])
        h.heap_insert(3)
        self.assertEqual(h, [4, 1, 3])
        h.heap_insert(2)
        self.assertEqual(h, [4, 2, 3, 1])
        h.heap_insert(16)
        self.assertEqual(h, [16,4, 3, 1, 2])
