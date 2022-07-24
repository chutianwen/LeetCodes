'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.max_sum = float('-inf')

		def dfs(root):
			if not root:
				return 0
			if not root.left and not root.right:
				self.max_sum = max(self.max_sum, root.val)
				return root.val

			left_max_sum = dfs(root.left)
			right_max_sum = dfs(root.right)
			print(left_max_sum, right_max_sum)
			sum_curve = root.val
			if left_max_sum > 0:
				sum_curve += left_max_sum

			if right_max_sum > 0:
				sum_curve += right_max_sum

			self.max_sum = max(self.max_sum, sum_curve)
			return max(left_max_sum + root.val, right_max_sum + root.val, root.val)

		dfs(root)
		return self.max_sum