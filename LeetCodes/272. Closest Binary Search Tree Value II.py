'''
272. Closest Binary Search Tree Value II
Hard

277

13

Favorite

Share
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
'''

class Solution:
	def closestKValues(self, root, target, k):

		# Helper, takes a path and makes it the path to the next node
		def nextpath(path, kid1, kid2):
			if path:
				if kid2(path):
					path += kid2(path),
					while kid1(path):
						path += kid1(path),
				else:
					kid = path.pop()
					while path and kid is kid2(path):
						kid = path.pop()

		# These customize nextpath as forward or backward iterator
		kidleft = lambda path: path[-1].left
		kidright = lambda path: path[-1].right

		# Build path to closest node
		path = []
		while root:
			path += root,
			root = root.left if target < root.val else root.right
		dist = lambda node: abs(node.val - target)
		path = path[:path.index(min(path, key=dist))+1]

		# Get the path to the next larger node
		path2 = path[:]
		nextpath(path2, kidleft, kidright)

		for x in path2:
			print(x.val)
		# Collect the closest k values by moving the two paths outwards
		vals = []
		for _ in range(k):
			if not path2 or path and dist(path[-1]) < dist(path2[-1]):
				vals += path[-1].val,
				nextpath(path, kidright, kidleft)
			else:
				vals += path2[-1].val,
				nextpath(path2, kidleft, kidright)
		return vals




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def closestKValues(self, root, target, k):
		"""
		:type root: TreeNode
		:type target: float
		:type k: int
		:rtype: List[int]
		"""
		min_diff = float('inf')
		dis = lambda x: abs(x.val - target)
		path_smaller = []
		while root:
			path_smaller.append(root)
			root = root.left if target < root.val else root.right
		path_smaller = path_smaller[: path_smaller.index(min(path_smaller, key=dis)) + 1]

		frontier_left = lambda path: path[-1].left
		frontier_right = lambda path: path[-1].right

		def next_path(path, frontier1, frontier2):
			# frontier1 is for checking if next node available, frontier2 is for pooling from stack
			if frontier1(path):
				path.append(frontier1(path))
				while frontier2(path):
					path.append(frontier2(path))
			else:
				node = path.pop()
				while path and node is frontier1(path):
					node = path.pop()

		path_larger = path_smaller[:]
		next_path(path_larger, frontier_right, frontier_left)
		for x in path_larger:
			print(x.val)
		res = []
		dis = lambda x: abs(x.val - target)
		for _ in range(k):
			if not path_larger or path_smaller and dis(path_smaller[-1]) < dis(path_larger[-1]):
				res.append(path_smaller[-1].val)
				next_path(path_smaller, frontier_left, frontier_right)
			else:
				res.append(path_larger[-1].val)
				next_path(path_larger, frontier_right, frontier_left)
		return res

class Solution:
	def closestKValues(self, root, target, k):

		abs_dis = lambda x: abs(x.val - target)

		stack_small = []
		while root:
			stack_small.append(root)
			root = root.left if target < root.val else root.right

		closest_cut = min(stack_small, key=abs_dis)
		stack_small = stack_small[:stack_small.index(closest_cut) + 1]
		stack_large = stack_small[:]

		def next(stack, fun1, fun2):

			if fun1(stack):
				stack.append(fun1(stack))
				while fun2(stack):
					stack.append(fun2(stack))
			else:
				cur = stack.pop()
				while stack and cur == fun1(stack):
					cur = stack.pop()

		frontier_left = lambda x: x[-1].left
		frontier_right = lambda x: x[-1].right

		next(stack_large, frontier_right, frontier_left)
		res = []
		for _ in range(k):
			if not stack_large or stack_small and abs_dis(stack_small[-1]) <= abs_dis(stack_large[-1]):
				res.append(stack_small[-1].val)
				next(stack_small, frontier_left, frontier_right)
			else:
				res.append(stack_large[-1].val)
				next(stack_large, frontier_right, frontier_left)
		return res
