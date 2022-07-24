'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

import numpy as np

class Solution:
	def maxAreaOfIsland(self, grid):
		"""
		Time: O(R*C), Space: O(R*C)
		:type grid: List[List[int]]
		:rtype: int
		"""
		h, w = np.shape(grid)
		directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

		def dfs(row, col, visited):
			if row < 0 or row >= h or col < 0 or col >= w or visited[row, col] or grid[row][col] == 0:
				return 0
			visited[row][col] = 1
			res = 1
			for direction in directions:
				row_cur, col_cur = row + direction[0], col + direction[1]
				res += dfs(row_cur, col_cur, visited)
			return res

		marker = np.zeros([h, w])
		areas = [dfs(row, col, visited=marker) for row in range(h) for col in range(w)]
		return max(areas)

	def maxAreaOfIslandIterative(self, grid):

		h, w = len(grid), len(grid[0])

		directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
		visited = [[0 for _ in range(w)] for _ in range(h)]

		max_area = 0
		for row in range(h):
			for col in range(w):
				if grid[row][col] == 0 or visited[row][col]:
					continue
				else:
					area = 0
					frontiers = [(row, col)]
					while len(frontiers) > 0:
						expandNode = frontiers.pop()
						visited[expandNode[0]][expandNode[1]] = 1
						area += 1

						for direction in directions:
							row_cur, col_cur = expandNode[0] + direction[0], expandNode[1] + direction[1]
							if 0 <= row_cur < h and 0 <= col_cur < w and grid[row_cur][col_cur]:
								# check if not explored and not in frontiers
								if not visited[row_cur][col_cur] and (row_cur, col_cur) not in frontiers:
								frontiers.append((row_cur, col_cur))

					max_area = max(max_area, area)

		return max_area


res = Solution().maxAreaOfIslandIterative([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
print(res)