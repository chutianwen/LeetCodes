'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''


class Solution:
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		n = 9
		row_set = [set() for _ in range(n)]
		col_set = [set() for _ in range(n)]
		block_set = [[set() for _ in range(n // 3)] for _ in range(n // 3)]

		# cannot using set() here, since each time pop() and add will not be consistent
		empty_set = []
		for row in range(n):
			for col in range(n):
				if board[row][col] == ".":
					empty_set.append((row, col))
				else:
					v = int(board[row][col])
					row_set[row].add(v)
					col_set[col].add(v)
					block_set[row // 3][col // 3].add(v)

		# each time fill the place closer to the previous one will be much faster to reach the solution.
		print("Before shuffle", empty_set, len(empty_set))
		# random.shuffle(empty_set)
		print("End Shuffle", empty_set, len(empty_set))

		def is_valid(row, col, v):
			return v not in row_set[row] and v not in col_set[col] and v not in block_set[row // 3][col // 3]

		def driver():

			if not empty_set or len(empty_set) == 0:
				return True

			# print("before", empty_set)
			row, col = empty_set.pop()
			print("before", row, col, empty_set, "size", len(empty_set))
			for candidate in range(1, 10):
				if is_valid(row, col, candidate):
					board[row][col] = str(candidate)
					row_set[row].add(candidate)
					col_set[col].add(candidate)
					block_set[row // 3][col // 3].add(candidate)
					if driver():
						return True
					row_set[row].remove(candidate)
					col_set[col].remove(candidate)
					block_set[row // 3][col // 3].remove(candidate)

			empty_set.append((row, col))
			print("after", row, col, empty_set, "size", len(empty_set))
			# print("after", empty_set)
			return False

		driver()

	def isValidSudoku(self, A):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		n = 9
		row_set = [set() for _ in range(n)]
		col_set = [set() for _ in range(n)]
		box_set = [[set() for _ in range(n // 3)] for _ in range(n // 3)]
		for i in range(n):
			for j in range(n):
				if A[i][j] == '.': continue
				x = int(A[i][j])
				if x < 1 or x > 9 or x in row_set[i] or x in col_set[j] or x in box_set[i // 3][j // 3]: return False
				row_set[i].add(x)
				col_set[j].add(x)
				box_set[i // 3][j // 3].add(x)
		return True


import unittest


class SudokuSolverTest(unittest.TestCase):
	"""Unit tests for isolation agents"""

	def setUp(self):
		self.board = [
			["5", "3", ".", ".", "7", ".", ".", ".", "."],
			["6", ".", ".", "1", "9", "5", ".", ".", "."],
			[".", "9", "8", ".", ".", ".", ".", "6", "."],
			["8", ".", ".", ".", "6", ".", ".", ".", "3"],
			["4", ".", ".", "8", ".", "3", ".", ".", "1"],
			["7", ".", ".", ".", "2", ".", ".", ".", "6"],
			[".", "6", ".", ".", ".", ".", "2", "8", "."],
			[".", ".", ".", "4", "1", "9", ".", ".", "5"],
			[".", ".", ".", ".", "8", ".", ".", "7", "9"]
		]

	def test_example(self):
		res = Solution().solveSudoku(self.board)
		print(res)

		for row in self.board:
			print(row)

		print(Solution().isValidSudoku(self.board))


if __name__ == '__main__':
	unittest.main()
