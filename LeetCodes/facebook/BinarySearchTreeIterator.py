'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.


'''

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.frontier = []
		self.track = root

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return self.track or self.frontier

	def next(self):
		"""
		:rtype: int
		"""Binary Tree
		while self.track:
			self.frontier.append(self.track)
			self.track = self.track.left

		expand = self.frontier.pop()
		self.track = expand.right
		return expand.val
		# Your BSTIterator will be called like this:
		# i, v = BSTIterator(root), []
		# while i.hasNext(): v.append(i.next())