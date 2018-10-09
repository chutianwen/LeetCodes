# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if not root: return res

		frontier = [root]
		while frontier:
			expand = frontier.pop()
			res.append(expand.val)
			for child in [expand.left, expand.right]:
				if child:
					frontier.append(child)
		return res[::-1]

	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if not root: return res
		frontier = []
		while root or frontier:
			while root:
				frontier.append(root)
				root = root.left
			expand = frontier.pop()
			res.append(expand.val)
			root = expand.right

		return res

	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if not root: return res

		frontier = [root]
		while frontier:
			expand = frontier.pop()
			res.append(expand.val)
			for child in [expand.right, expand.left]:
				if child:
					frontier.append(child)
		return res