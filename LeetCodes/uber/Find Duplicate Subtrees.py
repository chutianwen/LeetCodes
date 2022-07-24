'''
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
'''


class Solution:
	def isSameTree(self, p, q, res):
		if p and q:
			left_same = self.isSameTree(p.left, q.left, res)
			right_same = self.isSameTree(p.right, q.right, res)
			if p.val == q.val and left_same and right_same:
				res.add(p)
				return True
			else:
				return False
		return p is q

	def driver(self, p1, p2, res):

		if not self.isSameTree(p1, p2, res):
			if p1.left and self.driver(p1.left, p2, res):
				return

			if p1.right and self.driver(p1.right, p2, res):
				return

			if p2.left and self.driver(p1, p2.left, res):
				return

			if p2.right and	self.driver(p1, p2.right, res):
				return

	def findDuplicateSubtrees(self, root):
		"""
		:type root: TreeNode
		:rtype: List[TreeNode]
		"""
		res = set()
		if root and root.left and root.right:

			self.driver(root.left, root.right, res)
		return list(res)


class TreeNode:
	def __init__(self, v):
		self.val = v
		self.left = None
		self.right = None


class Solution2(object):
	def findDuplicateSubtrees(self, root):
		from collections import Counter
		count = Counter()
		ans = []

		def collect(node):
			if not node: return "#"
			serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
			count[serial] += 1
			if count[serial] == 2:
				ans.append(node)
			return serial

		collect(root)
		print(count)

		return ans

class Solution3(object):
	def findDuplicateSubtrees(self, root):
		import collections
		trees = collections.defaultdict()
		trees.default_factory = trees.__len__
		count = collections.Counter()
		ans = []
		def lookup(node):
			if node:
				left = lookup(node.left)
				right = lookup(node.right)
				uid = trees[node.val, left, right]
				print(uid, left, right)
				count[uid] += 1
				if count[uid] == 2:
					ans.append(node)
				return uid

		lookup(root)
		return ans

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.right = TreeNode(3)
# root.right.left = TreeNode(2)
# root.right.left.left = TreeNode(4)
# root.right.right = TreeNode(4)
root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(0)
root.right.right = TreeNode(0)
root.right.right.left = TreeNode(0)
root.right.right.right = TreeNode(0)


res = []
Solution().isSameTree(root.left, root.right, res)
for node in res:
	print(node.val)

print("-"*10)

res = Solution3().findDuplicateSubtrees(root)
for node in res:
	print(node.val)
