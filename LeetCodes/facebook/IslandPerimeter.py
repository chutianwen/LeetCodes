'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

'''

class Solution:

	def islandPerimeterArray(self, grid):

		perimeter = 0
		directions = [[1,0], [-1, 0], [0, -1], [0, 1]]
		h, w = len(grid), len(grid[0])
		for row in range(h):
			for col in range(w):
				if grid[row][col]:
					perimeter += 4
					for direction in directions:
						row_cur, col_cur = row + direction[0], col + direction[1]
						if 0 <= row_cur < h and 0 <= col_cur < w:
							perimeter -= grid[row_cur][col_cur]
		return perimeter

	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		h, w = len(grid), len(grid[0])
		explored = [[0 for _ in range(w)] for _ in range(h)]

		directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
		for row in range(h):
			for col in range(w):
				if grid[row][col] and not explored[row][col]:
					perimeter = 0
					frontier = [(row, col)]
					while frontier:
						expand = frontier.pop()
						explored[expand[0]][expand[1]] = 1
						perimeter += 4

						for direction in directions:
							row_cur, col_cur = expand[0] + direction[0], expand[1] + direction[1]
							if 0 <= row_cur < h and 0 <= col_cur < w and grid[row_cur][col_cur] and (row_cur, col_cur) not in frontier:
								if explored[row_cur][col_cur]:
									perimeter -= 2
								else:
									frontier.append((row_cur, col_cur))
					return perimeter

		return 0

res = Solution().islandPerimeterArray([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(res)