"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

from TreeNode import TreeNode

class Solution(object):
    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None) or (p.val != q.val):
            return False
        else:
            return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)

    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
