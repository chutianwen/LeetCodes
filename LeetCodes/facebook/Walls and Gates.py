'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''

class Solution:
	def wallsAndGates(self, rooms):
		"""
		:type rooms: List[List[int]]
		:rtype: void Do not return anything, modify rooms in-place instead.
		"""
		if not rooms and len(rooms) == 0:
			return

		h, w = len(rooms), len(rooms[0])
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

		def driver(rooms, cur, distance):
			'''
			We can either put return constraint up front, or during neighbor iteration.
			:param rooms:
			:param cur:
			:param distance:
			:return:
			'''
			for dir in directions:
				row_cur, col_cur = cur[0] + dir[0], cur[1] + dir[1]
				flag_boundary = 0 <= row_cur < h and 0 <= col_cur < w
				if flag_boundary and rooms[row_cur][col_cur] != -1 and distance < rooms[row_cur][col_cur]:
					rooms[row_cur][col_cur] = distance
					driver(rooms, [row_cur, col_cur], distance + 1)

		for row in range(h):
			for col in range(w):
				if rooms[row][col] == 0:
					driver(rooms, [row, col], 1)