'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

'''

class Trie(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.children = [None] * 26
		self.stop = False

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		cur = self
		for letter in word:
			id = ord(letter) - ord('a')
			if cur.children[id] is None:
				cur.children[id] = Trie()
			cur = cur.children[id]
		cur.stop = True

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		cur = self
		for letter in word:
			id = ord(letter) - ord('a')
			if cur.children[id] is None:
				return False
			cur = cur.children[id]
		return cur.stop

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		cur = self
		for letter in prefix:
			id = ord(letter) - ord('a')
			if cur.children[id] is None:
				return False
			cur = cur.children[id]
		return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("")
param_2 = obj.search("abc")
param_3 = obj.startsWith("ab")

print(param_2, param_3)