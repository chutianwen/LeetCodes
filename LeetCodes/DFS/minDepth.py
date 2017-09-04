"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

class Solution(object):

    def minDepth(self, root):
        """
        same function calls multiple times
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