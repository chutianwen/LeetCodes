'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''

from collections import Counter


class Solution(object):
	def gameOfLifeInfinite(self, live):
		ctr = Counter((I, J)
	                  for i, j in live
	                  for I in range(i-1, i+2)
	                  for J in range(j-1, j+2)
	                  if I != i or J != j)

		return {ij
		        for ij in ctr
		        if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""

		live_cell = {(row, col) for row in range(len(board)) for col in range(len(board[0])) if board[row][col]}

		live_cell_next = self.gameOfLifeInfinite(live_cell)
		print(live_cell_next)
		for i, row in enumerate(board):
			for j in range(len(row)):
				board[i][j] = int((i, j) in live_cell_next)

input = [
	[1, 1, 1],
	[0, 0, 1],
	[1, 1, 1],
	[0, 0, 0]
]

res = Solution().gameOfLife(input)
