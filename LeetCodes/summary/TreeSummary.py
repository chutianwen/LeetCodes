import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_leftmost_and_right_most(root):
    '''
    This fundamental traversal can be very handy for validating binary search tree
    :param root:
    :return:
    '''
    head = tail = root
    if root.left:
        lh, lt = get_leftmost_and_right_most(root.left)
        head = lh
    if root.right:
        rh, rt = get_leftmost_and_right_most(root.right)
        tail = rt
    return head, tail


def isValidBST(self, root):
    """
    Use idea of `get_leftmost_and_right_most` to valid <root, root.right, root.left> and also <root, mostRight in left tree and mostLeft in right
    tree>
    :type root: TreeNode
    :rtype: bool
    """
    def dfs(root):
        head = tail = root

        if root.left:
            lh, lt, flag = dfs(root.left)
            if not flag:
                return None, None, flag
            head = lh
            if root.val <= lt.val or root.val <= root.left.val:
                return None, None, False

        if root.right:
            rh, rt, flag = dfs(root.right)
            if not flag:
                return None, None, flag
            tail = rt
            if root.val >= rh.val or root.val >= root.right.val:
                return None, None, False

        return head, tail, True

    if root:
        _, _, flag = dfs(root)
        return flag
    else:
        return True

def inorder_traverse(root):
    '''
    Inorder traverse is also very helpful to validate binary search tree.
    :param root:
    :return:
    '''
    res = []
    frontier = []
    while root or frontier:
        # keep adding if root left part
        while root:
            frontier.append(root)
            root = root.left
        expand = frontier.pop()
        res.append(expand.val)
        root = expand.right

        # This can test if it is the end of node
        if not root and not frontier:
            print("Current expand is the rightmost node in the tree:\t{}".format(expand.val))
    print(res)

def pre_order_traverse(root):
    '''
    Both preorder and post order can be solve by dfs iteratively
    '''
    res = []
    frontier = [root]
    while frontier:
        expand = frontier.pop()
        res.append(expand.val)
        if expand.right:
            frontier.append(expand.right)
        if expand.left:
            frontier.append(expand.left)
    print(res)

def post_order_traverse(root):
    res = []
    frontier = [root]
    while frontier:
        expand = frontier.pop()
        res.append(expand.val)
        if expand.left:
            frontier.append(expand.left)
        if expand.right:
            frontier.append(expand.right)
    print(res[::-1])

def build_binary_tree_from_pre_inorder(preorder, inorder):
    if inorder:
        idx = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[idx])
        node.left = build_binary_tree_from_pre_inorder(preorder, inorder[:idx])
        node.right = build_binary_tree_from_pre_inorder(preorder, inorder[idx + 1:])
        return node

def build_binary_tree_from_post_inorder(postorder, inorder):
    if inorder:
        idx = inorder.index(postorder.pop())
        node = TreeNode(inorder[idx])
        node.left = build_binary_tree_from_pre_inorder(postorder, inorder[:idx])
        node.right = build_binary_tree_from_pre_inorder(postorder, inorder[idx + 1:])
        return node

def build_binary_tree_from_pre_post(pre, post):
    if pre:
        node = TreeNode(pre.pop(0))
        post.pop()
        if not post: return node
        idx = pre.index(post[-1])
        node.left = self.constructFromPrePost(pre[:idx], post[:idx])
        node.right = self.constructFromPrePost(pre[idx:], post[idx:])
        return node

def revert_binary_tree(root):
    if not root:
        return

    # we can do the swap before or after the divide
    root.left, root.right = root.right, root.left
    revert_binary_tree(root.left)
    revert_binary_tree(root.right)
    return root

def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p and q :
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        return p is q



class TreeTest(unittest.TestCase):

    def setUp(self):
        self.root = TreeNode(5)
        self.root.left = TreeNode(3)
        self.root.right = TreeNode(8)
        self.root.left.left = TreeNode(1)
        self.root.left.left.left = TreeNode(0)
        self.root.left.left.right = TreeNode(2)
        self.root.right.right = TreeNode(10)
        self.root.right.right.left = TreeNode(9)
        self.root.right.right.right = TreeNode(11)

    def test_leftmost_and_rightmost(self):
        if self.root:
            head, tail = get_leftmost_and_right_most(self.root)
            print(head.val, tail.val )

    def test_order_traverse(self):
        print("Inorder traverse")
        inorder_traverse(self.root)

        print("\n")
        print("Preorder traverse")
        pre_order_traverse(self.root)

        print('\n')
        print("Postorder traverse")
        post_order_traverse(self.root)

    def test_build_tree_from_order(self):
        print("Test building tree from preorder and inorder traverse")
        pre_order = [5, 3, 1, 0, 2, 8, 10, 9, 11]
        inorder = [0, 1, 2, 3, 5, 8, 9, 10, 11]
        post_order = [0, 2, 1, 3, 9, 11, 10, 8, 5]

        node = build_binary_tree_from_pre_inorder(pre_order, inorder)
        pre_order_traverse(node)
        inorder_traverse(node)

        node = build_binary_tree_from_post_inorder(post_order, inorder)
        post_order_traverse(node)

if __name__ == "__main__":
    unittest.main()