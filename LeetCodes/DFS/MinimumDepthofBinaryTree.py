"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

from TreeNode import TreeNode

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if self.minDepth(root.left) == 0:
            return self.minDepth(root.right) + 1

        if self.minDepth(root.right) == 0:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        height_left = self.minDepth(root.left)
        height_right = self.minDepth(root.right)

        if height_left == 0:
            return height_right + 1

        if height_right == 0:
            return height_left + 1

        return min(height_left, height_right) + 1