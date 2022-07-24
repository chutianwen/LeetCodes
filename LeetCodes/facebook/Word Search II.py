'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class TrieNode:
	def __init__(self):
		self.stop = False
		self.children = [None] * 26

	def add(self, words):
		root = self
		for letter in words:
			idx = ord(letter) - ord('a')
			if not root.children[idx]:
				root.children[idx] = TrieNode()
			root = root.children[idx]

		root.stop = True

	def find(self, word):
		root = self
		for letter in word:
			idx = ord(letter) - ord('a')
			if not root.children[idx]:
				return False, root.stop
			root = root.children[idx]
		return True, root.stop

class Solution:

	def findWords(self, board, words):

		if not board or len(board) == 0 or not words or len(words) == 0:
			return []

		dictionary = TrieNode()
		for word in words:
			dictionary.add(word)

		h, w = len(board), len(board[0])
		explored = [[0 for _ in range(w)] for _ in range(h)]
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		res = set()

		def driver(row, col, word_cur):

			is_go_on, is_word = dictionary.find(word_cur)
			if not is_go_on:
				return

			if is_word:
				res.add(word_cur)

			explored[row][col] = 1
			for direction in directions:
				row_next, col_next = row + direction[0], col + direction[1]
				in_boundary = 0 <= row_next < h and 0 <= col_next < w
				if in_boundary and not explored[row_next][col_next]:
					driver(row_next, col_next, word_cur + board[row_next][col_next])

			explored[row][col] = 0

		for row in range(h):
			for col in range(w):
				driver(row, col, board[row][col])

		return list(res)


	def findWordsDFSWithSet(self, board, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		if not board or len(board) == 0 or not words or len(words) == 0:
			return []

		h, w = len(board), len(board[0])
		dictionary = set(words)
		len_limit = max(map(len, words))
		explored = [[0 for _ in range(w)] for _ in range(h)]
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		res = set()

		def driver(row, col, word_cur):

			if len(word_cur) > len_limit:
				return

			explored[row][col] = 1
			if word_cur in dictionary:
				res.add(word_cur)

			for direction in directions:
				row_next, col_next = row + direction[0], col + direction[1]
				in_boundary = 0 <= row_next < h and 0 <= col_next < w
				if in_boundary and not explored[row_next][col_next]:
					driver(row_next, col_next, word_cur + board[row_next][col_next])

			explored[row][col] = 0

		for row in range(h):
			for col in range(w):
				driver(row, col, board[row][col])

		return list(res)

words = ["oath","pea","eat","rain"]

input = [
	['o','a','a','n'],
	['e','t','a','e'],
	['i','h','k','r'],
	['i','f','l','v']
]

result = Solution().findWords(input, words)
print(result)