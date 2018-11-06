'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:



Note:

The total number of elements of the given matrix will not exceed 10,000.
'''


class Solution(object):
	def findDiagonalOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if not matrix: return []
		m, n = len(matrix), len(matrix[0])
		res = []

		def in_boundary(x):
			return 0 <= x[0] < m and 0 <= x[1] < n

		def traverse(pos):
			buffer = []
			while in_boundary(pos):
				buffer.append(matrix[pos[0]][pos[1]])
				pos[0] -= 1
				pos[1] += 1
			res.append(buffer)

		for row in range(m):
			traverse([row, 0])

		for col in range(1, n):
			traverse([m - 1, col])

		for idx in range(1, len(res), 2):
			res[idx].reverse()

		return [entry for r in res for entry in r]
