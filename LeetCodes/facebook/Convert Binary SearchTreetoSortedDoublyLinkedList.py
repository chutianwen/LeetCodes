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



class Solution2(object):
	def treeToDoublyList(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		def traverse(node):
			if not node.left and not node.right:
				return node, node

			if node.left:
				hl, tl = traverse(node.left)
				tl.right, node.left = node, tl
			else:
				hl, tl = node, node

			if node.right:
				hr, tr = traverse(node.right)
				hr.left, node.right = node, hr
			else:
				hr, tr = node, node
			return hl, tr

		if not root:
			return None
		hl, tr = traverse(root)
		hl.left, tr.right = tr, hl
		return hl


class Solution3(object):
	def treeToDoublyList(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		if root:
			head, tail = self.helper(root)
			return head
		return None


	def helper(self, root):
		"""Idea: Construct a DLL for each subtree, then return the head and tail"""
		head, tail = root, root
		if root.left:
			lh, lt = self.helper(root.left)
			lt.right = root
			root.left = lt
			head = lh
		if root.right:
			rh, rt = self.helper(root.right)
			rh.left = root
			root.right = rh
			tail = rt
		head.left = tail
		tail.right = head
		return (head, tail)

class SolutionBest(object):
	def treeToDoublyList(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""

		def dfs(root):
			head = tail = root
			if root.left:
				lh, lt = dfs(root.left)
				head = lh
				lt.right, root.left = root, lt

			if root.right:
				rh, rt = dfs(root.right)
				tail = rt
				root.right, rh.left = rh, root
			return head, tail

		if root:
			head, tail = dfs(root)
			head.left, tail.right = tail, head
			return head
