# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1 = TreeNode(3)
t2 = TreeNode(4)
t3 = TreeNode(3)

print(t1 is t3)
print(t1 is t2)
