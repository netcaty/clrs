class Node:
    def __init__(self, k, left=None, right=None, p= None):
        #self.p = p
        self.left = left
        self.right = right
        self.k = k

    def __lt__(self, other):
        assert isinstance(other, Node)
        return self.k < other.k

    def __eq__(self, other):
        assert isinstance(other, Node)
        return self.k == other.k


def inorder_tree_walk(root):
    if root is not None:
        inorder_tree_walk(root.left)
        print(root.k)
        inorder_tree_walk(root.right)

def preorder_tree_walk(root):
    if root is not None:
        print(root.k)
        inorder_tree_walk(root.left)
        inorder_tree_walk(root.right)

def postorder_tree_walk(root):
    if root is not None:
        inorder_tree_walk(root.left)
        inorder_tree_walk(root.right)
        print(root.k)


def inorder_tree_walk_with_stack(root):
    current = root
    s = []
    done = False

    while not done:
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if s:
                current = s.pop()
                print(current.k)
                current = current.right
            else:
                done = True


def MorrisTraversal(root):
    '''不使用递归和Stack的中序遍历'''
    current = root

    while current is not None:
        if current.left is None:
            print(current.k)
            current = current.right
        else:
            pre = current.left
            while pre.right is not None and pre.right is not current:
                pre = pre.right

            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                print(current.k)
                current = current.right


def constructBST(iterable):
    '''Given preorder traversal of a binary search tree, construct the BST.
    1. 新建一个空栈
    2. 让第一个元素成为root并压栈
    3. 如果序列中的下一个元素比栈顶元素的值大，且栈不为空，就不停弹出栈顶元素。
        让这个元素成为最后一个弹出元素的右孩子， 并将它压栈。
    4. 如果序列中的下一个元素比栈顶元素的值小，就让这个元素成为栈顶元素的左孩子，
        并压栈。
    5. 重复步骤2-4直到输入序列中的所有元素遍历完毕。
    '''
    stack = []

    it = iter(iterable)
    root = Node(next(it))
    stack.append(root)

    for e in it:
        node = Node(e)
        last = None
        if node < stack[-1]:
            stack[-1].left = node
        else:
            while stack and node > stack[-1]:
                last = stack.pop()
            if last is not None:
                last.right = node
        stack.append(node)

    return root


def tree_search(root, k):
    if root is None or k == root.k:
        return root
    if k < root.k:
        return tree_search(root.left, k)
    return tree_search(root.right, k)


def iter_tree_search(root, k):
    '''迭代版本的树搜索'''
    while root is not None and k != root.k:
        if k < root.k:
            root = root.left
        else:
            root = root.right
    return root


def tree_minimum(root):
    while root.left is not None:
        root = root.left
    return root


def tree_maximum(root):
    while root.right is not None:
        root = root.right
    return root
