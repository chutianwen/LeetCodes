'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
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
	def verticalOrder(self, root):

		if not root:
			return []

		frontier = deque([(root, 0)])
		res = [[root.val]]
		set_idx = set()
		set_idx.add(0)
		num_expand_left = 0

		while frontier:

			expand, idx = frontier.popleft()

			for kid, idx in [(expand.left, idx - 1), (expand.right, idx + 1)]:
				if kid:
					if idx not in set_idx:
						if idx < 0:
							res.insert(0, [kid.val])
							num_expand_left += 1
						else:
							res.append([kid.val])
						set_idx.add(idx)
					else:
						res[idx + num_expand_left].append(kid.val)

					frontier.append((kid, idx))
		return res

	def verticalOrderDFS(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""

		def helper(root):

			if not root:
				return [], -1

			res = []

			left_vertical, left_pos = helper(root.left)
			right_vertical, right_pos = helper(root.right)

			print(root.val, left_vertical, right_vertical)
			# left part
			i, j = left_pos, right_pos - 2

			res.append([root.val])
			if left_pos + 1 < len(left_vertical):
				res[0].extend(left_vertical[left_pos + 1])
			if right_pos - 1 >= 0:
				res[0].extend(right_vertical[right_pos - 1])

			while len(left_vertical) > i >= 0 or len(right_vertical) > j >= 0:

				if i >= 0 and j >= 0:
					res.append(left_vertical[i] + right_vertical[j])
				elif i >= 0 and j < 0:
					res.append(left_vertical[i])
				elif i < 0 and j >= 0:
					res.append(right_vertical[j])

				i -= 1
				j -= 1

			res = res[::-1]

			root_pos = len(res) - 1

			i, j = left_pos + 2, right_pos
			print(root.val, i, len(left_vertical), j, len(right_vertical))

			while 0 <= i < len(left_vertical) or 0 <= j < len(right_vertical):

				if 0 <= i < len(left_vertical) and 0 <= j < len(right_vertical):
					res.append(right_vertical[j] + left_vertical[i])
				elif i >= len(left_vertical) or i < 0 and j < len(right_vertical):
					res.append(right_vertical[j])
				elif i < len(left_vertical) and j >= len(right_vertical) or j < 0:
					print(root.val, left_vertical[i])
					res.append(left_vertical[i])

				i += 1
				j += 1
			return res, root_pos

		result, _ = helper(root)
		return result


root = TreeNode(6)
root.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(2)
root.left.right.right = TreeNode(5)
root.left.right.right.left = TreeNode(4)

res = Solution().verticalOrder(root)
print(res)

class Solution2:

	def verticalOrder(self, root):
		from collections import defaultdict

		cols = collections.defaultdict(list)
		queue = [(root, 0)]
		for node, i in queue:
			if node:
				cols[i].append(node.val)
				queue += (node.left, i - 1), (node.right, i + 1)
		return [cols[i] for i in sorted(cols)]