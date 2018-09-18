'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10
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

res = Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
print(res)