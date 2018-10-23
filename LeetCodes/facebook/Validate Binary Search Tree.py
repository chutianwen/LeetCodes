'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""

		def dfs(root):
			head = tail = root

			if root.left:
				lh, lt, flag = dfs(root.left)
				if not flag:
					return None, None, flag
				head = lh
				if not root.val > lt.val:
					return None, None, False

			if root.right:
				rh, rt, flag = dfs(root.right)
				if not flag:
					return None, None, flag
				tail = rt
				if not root.val < rh.val:
					return None, None, False

			return head, tail, True

		if root:
			_, _, flag = dfs(root)
			return flag
		else:
			return True

class Solution2(object):
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		res = []
		def dfs(root):
			if not root:
				return
			dfs(root.left)
			res.append(root.val)
			dfs(root.right)

		dfs(root)
		for idx in range(1, len(res)):
			if res[idx] <= res[idx - 1]:
				return False
		return True
