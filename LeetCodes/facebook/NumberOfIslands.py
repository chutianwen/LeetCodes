'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""

		if grid is None or len(grid) == 0: return 0

		h, w = len(grid), len(grid[0])
		directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
		explored = [[0 for _ in range(w)] for _ in range(h)]

		def dfs(row, col):

			explored[row][col] = 1

			for direction in directions:
				row_cur, col_cur = row + direction[0], col + direction[1]
				if 0 <= row_cur < h and 0 <= col_cur < w and not explored[row_cur][col_cur] and grid[row_cur][col_cur] == "1":
					dfs(row_cur, col_cur)

			return

		cnt = 0
		for row in range(h):
			for col in range(w):
				if grid[row][col] == "1" and not explored[row][col]:
					dfs(row, col)
					cnt += 1

		return cnt