'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution(object):
	def setZeroes2(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		if not matrix or len(matrix) == 0:
			return

		height, width = len(matrix), len(matrix[0])
		i = j = 0

		while i < height and j < width:

			if not matrix[i][j]:
				for row in range(height):
					matrix[row][j] = 0
				for col in range(width):
					matrix[i][col] = 0

			j += 1
			if j == width:
				j = 0
				i += 1

	def setZeroes(self, matrix):
		# First row has zero?
		m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
		# Use first row/column as marker, scan the matrix
		for i in range(1, m):
			for j in range(n):
				if matrix[i][j] == 0:
					matrix[0][j] = matrix[i][0] = 0
		# Set the zeros
		for i in range(1, m):
			for j in range(n - 1, -1, -1):
				if matrix[i][0] == 0 or matrix[0][j] == 0:
					matrix[i][j] = 0
		# Set the zeros for the first row
		if firstRowHasZero:
			matrix[0] = [0] * n

input = [
	[0,1,2,0],
	[3,4,5,2],
	[1,3,1,5]
]

Solution().setZeroes(input)
print(input)