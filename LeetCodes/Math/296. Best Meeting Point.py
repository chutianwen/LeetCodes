'''
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.
'''

class Solution(object):
	def minTotalDistance(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if not grid:
			return 0
		rows, cols = [], []
		h, w = len(grid), len(grid[0])
		for row in range(h):
			for col in range(w):
				if grid[row][col]:
					rows.append(row)

		for col in range(w):
			for row in range(h):
				if grid[row][col]:
					cols.append(col)

		def get_dist(data):
			i, j = 0, len(data) - 1
			dist = 0
			while i < j:
				dist += data[j] - data[i]
				i += 1
				j -= 1
			return dist

		return get_dist(rows) + get_dist(cols)