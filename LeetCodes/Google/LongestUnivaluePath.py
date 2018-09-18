'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


	def longestUnivaluePath(self, root):
		"""
		Use global variable to store longest path
		:type root: TreeNode
		:rtype: int
		"""
		self.max_path = 0
		def dfs(root):

			if not root:
				return 0

			left_length = dfs(root.left)
			right_length = dfs(root.right)

			left_arrow = right_arrow = 0
			if root.left and root.val == root.left.val:
				left_arrow = left_length + 1

			if root.right and root.val == root.right.val:
				right_arrow = right_length + 1

			self.max_path = max(self.max_path, left_arrow + right_arrow)
			return max(left_arrow, right_arrow)

		dfs(root)
		return self.max_path