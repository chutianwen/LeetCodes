"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""

from TreeNode import TreeNode
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        judge if current node has left leave:
        if root.left and root.left.left is None and root.left.right is None:
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if root is None:
            return 0
        elif root.left and root.left.left is None and root.left.right is None:
            # cannot return now, root is the corner case. If return, then root.right won't be traversed.
            res += root.left.val

        res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res