'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''


class Solution(object):
	def largestRectangleArea(self, heights):
		"""
		:type heights: List[int]
		:rtype: int
		"""
		increase_height = [-1]

		max_area = 0
		for idx, height in enumerate(heights):
			while increase_height[-1] != -1 and heights[increase_height[-1]] >= height:
				max_area = max(max_area, heights[increase_height.pop()] * (idx - increase_height[-1] - 1))
			increase_height.append(idx)
		while increase_height[-1] != -1:
			max_area = max(max_area, heights[increase_height.pop()] * (len(heights) - increase_height[-1] - 1))
		return max_area

	def maximalRectangle(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		if not matrix or len(matrix) == 0:
			return 0

		hist = None
		max_area = 0
		for row in matrix:
			if hist is None:
				hist = list(map(int, row))
			else:
				for idx, letter in enumerate(row):
					if letter == "1":
						hist[idx] += 1
					elif letter == "0":
						hist[idx] = 0

			max_area = max(max_area, self.largestRectangleArea(hist))
		return max_area


input = [
	["1", "0", "1", "0", "0"],
	["1", "0", "1", "1", "1"],
	["1", "1", "1", "1", "1"],
	["1", "0", "0", "1", "0"]
]

res = Solution().maximalRectangle(input)
print(res)
