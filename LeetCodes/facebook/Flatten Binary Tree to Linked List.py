'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def flatten2(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		if not root:
			return

		right = root.right
		self.flatten(root.left)
		root.right = root.left
		root.left = None
		while root.right:
			root = root.right
		root.left = None
		self.flatten(right)
		root.right = right

	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		if root:
			self.flatten(root.left)
			self.flatten(root.right)
			right = root.right
			root.right, root.left = root.left, None
			while root.right:
				root = root.right
			root.left, root.right = None, right

