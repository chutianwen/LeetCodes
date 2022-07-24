"""
# Definition for a QuadTree node.

"""
class Node:
	def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
		self.val = val
		self.isLeaf = isLeaf
		self.topLeft = topLeft
		self.topRight = topRight
		self.bottomLeft = bottomLeft
		self.bottomRight = bottomRight

class Solution:
	def construct(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: Node
		"""
		if not grid or len(grid) == 0:
			return None

		h, w = len(grid), len(grid[0])
		def driver(bot_left, top_right):

			if top_right[0] == bot_left[0] or bot_left[1] == top_right[1]:
				return None

			is_leaf = True
			v = grid[top_right[0]][bot_left[1]]
			for row in range(top_right[0], bot_left[0]):
				for col in range(bot_left[1], top_right[1]):
					if grid[row][col] != v:
						is_leaf, v = False, "*"
						break

			# print(bot_left, top_right, pre, is_leaf)
			if is_leaf:
				return Node(v, is_leaf, None, None, None, None)
			elif not is_leaf:

				mid_row = top_right[0] + (bot_left[0] - top_right[0]) // 2
				mid_col = bot_left[1] + (top_right[1] - bot_left[1]) // 2

				node_top_left = driver([mid_row, bot_left[1]], [top_right[0], mid_col])
				node_top_right = driver([mid_row, mid_col], top_right)
				node_bot_left = driver(bot_left, [mid_row, mid_col])
				node_bot_right = driver([bot_left[0], mid_col], [mid_row, top_right[1]])
				return Node(pre, is_leaf, node_top_left, node_top_right, node_bot_left, node_bot_right)

		return driver([h, 0], [0, w])

	def construct2(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: Node
		"""
		if not grid or len(grid) == 0:
			return None

		h, w = len(grid), len(grid[0])
		def driver(bot_left, top_right):

			is_leaf = True
			pre = "*"
			for row in range(top_right[0], bot_left[0] + 1):
				for col in range(bot_left[1], top_right[1] + 1):
					if pre != "*" and grid[row][col] != pre:
						is_leaf = False
						pre = "*"
						break
					pre = grid[row][col]

			print(bot_left, top_right, pre, is_leaf)
			if is_leaf:
				if pre == "*":
					return None
				else:
				we	return Node(pre, is_leaf, None, None, None, None)
			else:

				mid_row = top_right[0] + (bot_left[0] - top_right[0]) // 2
				mid_col = bot_left[1] + (top_right[1] - bot_left[1]) // 2

				node_top_left = driver([mid_row, bot_left[1]], [top_right[0], mid_col])
				node_top_right = driver([mid_row, mid_col + 1], top_right)
				node_bot_left = driver(bot_left, [mid_row + 1, mid_col])
				node_bot_right = driver([bot_left[0], mid_col + 1], [mid_row + 1, top_right[1]])
				return Node(pre, is_leaf, node_top_left, node_top_right, node_bot_left, node_bot_right)

		return driver([h - 1, 0], [0, w - 1])

input = [[1,1,1,1,0,0,0,0],
         [1,1,1,1,0,0,0,0],
         [1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1],
         [1,1,1,1,0,0,0,0],
         [1,1,1,1,0,0,0,0],
         [1,1,1,1,0,0,0,0],
         [1,1,1,1,0,0,0,0]]

res = Solution().construct2([[1,0,1,1,0,0,0,0]])
