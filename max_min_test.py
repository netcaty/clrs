from unittest import TestCase

from max_min import *


class TestMaxMin(TestCase):
    def test_min_max(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        self.assertEqual(min_max(a), (1, 16))
