'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:

	def levelOrder(self, root):

		res = []
		if not root:
			return res

		res.append([root.val])
		if not root.left and not root.right:
			return res

		res_left = self.levelOrder(root.left)
		res_right = self.levelOrder(root.right)

		id = 0

		# merge right to left
		while id < len(res_right):
			if id < len(res_left):
				res_left[id].extend(res_right[id])
			else:
				res_left.append(res_right[id])
			id += 1

		res.extend(res_left)

		return res

	def levelOrderIterative(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		res = []
		if not root: return res

		frontier = deque()
		frontier.append((root, 1))
		while frontier:
			expand, depth = frontier.popleft()
			if depth > len(res):
				res.append([])
			res[depth - 1].append(expand.val)
			for child in [expand.left, expand.right]:
				if child:
					frontier.append((child, depth + 1))
		return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

res = Solution().levelOrder(root)
print(res)