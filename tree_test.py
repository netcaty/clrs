import unittest

from tree import *


class TestTree(unittest.TestCase):
    def test_tree_walk(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(4)
        root.left.left = Node(1)
        root.left.right = Node(16)
        root.right.right = Node(17)

        print('walk tree with stack')
        inorder_tree_walk_with_stack(root)
        print('walk tree with recursion')
        inorder_tree_walk(root)
        print('walk tree without reursion and stack')
        MorrisTraversal(root)

    def test_tree_search(self):
        pass

    def test_constuctBST(self):
        s = [10, 5, 1, 7, 40, 50]
        root = constructBST(s)
        # 构建完之后的BST应该是这个样子
        #       10
        #      /   \
        #     5     40
        #    / \     \
        #   1   7     50
        inorder_tree_walk_with_stack(root)

    def test_tree_minimum(self):
        s = [10, 5, 1, 7, 40, 50]
        root = constructBST(s)
        min = tree_minimum(root)
        self.assertEqual(min.k, 1)
