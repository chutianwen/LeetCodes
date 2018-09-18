'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

'''


class Solution(object):
	def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		if not matrix or len(matrix) == 0:
			return 0

		pre_row_largest = list(map(int, matrix[0]))
		max_area = max(pre_row_largest)

		for row in matrix[1:]:
			next_cache = [0 for _ in range(len(matrix[-1]))]
			pre_left = 0
			for idx, col in enumerate(row):
				if col == '1':
					if idx - 1 >= 0:
						cur_max = min(pre_row_largest[idx], pre_row_largest[idx - 1], pre_left) + 1
					else:
						cur_max = min(pre_row_largest[idx], pre_left) + 1
					max_area = max(max_area, cur_max ** 2)
					pre_left = cur_max
					next_cache[idx] = cur_max

				elif col == '0':
					pre_left = 0
					next_cache[idx] = 0

			pre_row_largest = next_cache
		return max_area

input = [["0","0","0","1","0","1","1","1"],
         ["0","1","1","0","0","1","0","1"],
         ["1","0","1","1","1","1","0","1"],
         ["0","0","0","1","0","0","0","0"],
         ["0","0","1","0","0","0","1","0"],
         ["1","1","1","0","0","1","1","1"],
         ["1","0","0","1","1","0","0","1"],
         ["0","1","0","0","1","1","0","0"],
         ["1","0","0","1","0","0","0","0"]]
res = Solution().maximalSquare(input)
print(res)