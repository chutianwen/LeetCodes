'''
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def minDiffInBST(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root: return None

		res = float('inf')
		frontier = []
		pre = None
		while frontier or root:
			while root:
				frontier.append(root)
				root = root.left
			expand = frontier.pop()
			if not pre is None:
				res = min(res, expand.val - pre)
			pre = expand.val
			root = expand.right
		return res



class A:
	def __init__(self, a):
		self.a = a


res = [A(4), A(2), A(3)]
res.sort(key=lambda x: x.a)
for r in res:
	print(r, r.a)