'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def countUnivalSubtrees(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		cnt = [0]
		def dfs(root):
			if not root:
				return True

			flag = True
			if root.left:
				left_is_uni = dfs(root.left)
				if not left_is_uni or (left_is_uni and root.left.val != root.val):
					flag = False

			if root.right:
				right_is_uni = dfs(root.right)
				if not right_is_uni or (right_is_uni and root.right.val != root.val):
					flag = False

			if flag:
				cnt[0] += 1
			return flag

		dfs(root)
		return cnt[0]