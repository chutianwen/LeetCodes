'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''


class TrieNode:

	def __init__(self):
		self.stop = False
		self.children = [None] * 26

	def add_word(self, word):
		cur = self
		for letter in word:
			idx = ord(letter) - ord('a')
			if not cur.children[idx]:
				cur.children[idx] = TrieNode()
			cur = cur.children[idx]

		cur.stop = True

	def search_word(self, word):
		cur = self
		for letter in word:
			idx = ord(letter) - ord('a')
			if not cur.children[idx]:
				return False
			cur = cur.children[idx]
		return cur.stop

class WordDictionary(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.dictionary = TrieNode()

	def addWord(self, word):
		"""
		Adds a word into the data structure.
		:type word: str
		:rtype: void
		"""
		self.dictionary.add_word(word)

	def search(self, word):

		frontier = [(self.dictionary, word)]

		while frontier:

			expand, path = frontier.pop()
			if not path and expand.stop:
				return True
			elif not path:
				continue

			if path[0] != ".":
				idx = ord(path[0]) - ord('a')
				future = expand.children[idx]
				if future:
					frontier.append((future, path[1:]))
			else:
				for future in expand.children:
					if future:
						frontier.append((future, path[1:]))

		return False

	def search1(self, word):
		"""
		Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
		:type word: str
		:rtype: bool
		"""

		def driver(root, word):
			if not word:
				return root.stop

			letter = word[0]
			if letter != ".":
				idx = ord(letter) - ord('a')
				if root.children[idx]:
					return driver(root.children[idx], word[1:])
				else:
					return False
			else:
				for path in root.children:
					if path:
						flag = driver(path, word[1:])
						if flag:
							return True
				return False

		return driver(self.dictionary, word)

tool = WordDictionary()
tool.addWord("at")
tool.addWord("and")
tool.addWord("an")
tool.addWord("add")
tool.addWord("at")
tool.addWord("bat")

print(tool.search("a.d"))
