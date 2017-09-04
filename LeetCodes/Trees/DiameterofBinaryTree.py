"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
 length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

from TreeNode import TreeNode

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        Using another variable max_v to store the max diameter. We cannot return the max_diameter during recursive,
        so we need a global variable to help us.
        :type root: TreeNode
        :rtype: int
        """
        def driver(root, max_v):
            if root is None:
                return 0
            else:
                height_left = driver(root.left, max_v)
                height_right = driver(root.right, max_v)
                max_v[0] = max(max_v[0], height_left + height_right)
                return max(height_left, height_right) + 1
        max_v = [0]
        _ = driver(root, max_v)
        return max_v[0]