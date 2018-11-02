'''
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
'''

class TrieNode:
	def __init__(self):
		self.stop = False
		self.children = dict()

class Solution:

	def __init__(self):
		self.root = TrieNode()

	def add_word(self, word):
		cur = self.root
		for letter in word:
			if letter not in cur.children:
				cur.children[letter] = TrieNode()
			cur = cur.children[letter]
		cur.stop = True

	def build_trie(self, words):
		for word in words:
			self.add_word(word)

	def longestWord(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""
		self.build_trie(words)
		self.longest_word = ""

		def dfs(node, path):
			for branch in node.children:
				if node.children[branch].stop:
					dfs(node.children[branch], path+branch)

			if len(path) > len(self.longest_word) or len(path) == len(self.longest_word) and path < self.longest_word:
				self.longest_word = path
		dfs(self.root, "")
		return self.longest_word
