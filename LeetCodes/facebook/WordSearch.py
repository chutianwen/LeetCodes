'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		h, w = len(board), len(board[0])
		directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

		def dfs(word, row, col, visited):

			if not word or len(word) == 0:
				return True
			else:
				if board[row][col] != word[0]:
					return False
				else:
					if len(word) == 1:
						return True

					visited[row][col] = 1
					for direction in directions:
						row_cur, col_cur = row + direction[0], col + direction[1]
						if 0 <= row_cur < h and 0 <= col_cur < w and not visited[row_cur][col_cur]:
							if dfs(word[1:], row_cur, col_cur, visited):
								# This may not need
								visited[row][col] = 0
								return True

					# backTracking for other directions
					visited[row][col] = 0
					return False

		marker = [[0 for _ in range(w)] for _ in range(h)]
		for row in range(h):
			for col in range(w):

				if dfs(word, row, col, marker):
					print(marker)
					return True
				else:
					print(marker)
		return False


board = [
	['A', 'B', 'C', 'E'],
	['S', 'F', 'E', 'S'],
	['A', 'D', 'E', 'E']
]
word = "BCESEEEFS"

# board = [["a", "b"], ["c", "d"]]

res = Solution().exist(board, word)
print(res)
