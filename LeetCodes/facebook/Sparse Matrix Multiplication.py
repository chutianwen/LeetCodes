'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

'''

class Solution(object):
	def multiply(self, A, B):
		"""
		:type A: List[List[int]]
		:type B: List[List[int]]
		:rtype: List[List[int]]
		"""
		if not A or not B or len(A) == 0 or len(B) == 0:
			return 0
		m, n = len(A), len(A[0])
		h, k = len(B), len(B[0])

		if n != h:
			return 0

		from collections import defaultdict

		# {(row, col): v}
		map_A = {(row, col): A[row][col] for row in range(m) for col in range(n) if A[row][col]}

		# {row: {col: v}}, A's col corresponds to B's row
		map_B = defaultdict(dict)

		for row in range(h):
			for col in range(k):
				if B[row][col]:
					map_B[row][col] = B[row][col]

		result = [[0 for _ in range(k)] for _ in range(m)]
		for row_a, col_a in map_A:
			for col_b in map_B[col_a]:
				result[row_a][col_b] += map_A[(row_a, col_a)] * map_B[col_a][col_b]

		return result

A = [
	[ 1, 0, 0],
	[-1, 0, 3]
]

B = [
	[ 7, 0, 0 ],
	[ 0, 0, 0 ],
	[ 0, 0, 1 ]
]

res = Solution().multiply(A, B)
for row in res:
	print(row)