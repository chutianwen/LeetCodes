'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math
class Solution:

	def closestValue(self, root, target):

		def helper(root, target):
			if not root:
				return float("inf")

			diff = root.val - target

			if diff == 0:
				return diff
			elif diff > 0:
				dif_kid = helper(root.left, target)
			else:
				dif_kid = helper(root.right, target)

			return dif_kid if abs(dif_kid) < abs(diff) else diff

		res = helper(root, target) + target
		return int(res)

	def closestValue2(self, root, target):
		"""
		:type root: TreeNode
		:type target: float
		:rtype: int
		"""
		self.res = float("inf")

		def helper(root, target):

			if not root:
				return

			if root.val == target:
				self.res = root.val
				return

			if math.fabs(self.res - target) > math.fabs(root.val - target):
				self.res = root.val

			if root.val > target:
				helper(root.left, target)
			else:
				helper(root.right, target)

		helper(root, target)
		return self.res

