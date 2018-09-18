'''
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:





We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
	def treeToDoublyList(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""

		pre = new_head = None

		if not root: return pre

		frontier = []

		while root or frontier:

			while root:
				frontier.append(root)
				root = root.left

			expand = frontier.pop()

			if pre is None:
				pre = new_head = expand
			else:
				# next
				expand.left = pre
				pre.right = expand
				pre = expand

			root = expand.right
			# end
			if expand.right is None and len(frontier) == 0:
				expand.right = new_head
				new_head.left = expand

		return new_head




