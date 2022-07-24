'''
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.


Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

Note:
The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
'''

from collections import defaultdict

class TrieNode:
	def __init__(self):
		# the last is for space
		self.children = dict()
		self.hot_degree = 0

class AutocompleteSystem:

	def __init__(self, sentences, times):
		"""
		:type sentences: List[str]
		:type times: List[int]
		"""
		self.root = TrieNode()
		# build the tree
		for sentence, hot_degree in zip(sentences, times):
			self.add_word(sentence, hot_degree)

		self.cur_node = self.root
		self.prefix = ""

	def add_word(self, sentence, time):
		cur = self.root
		for letter in sentence:
			if letter not in cur.children:
				cur.children[letter] = TrieNode()
			cur = cur.children[letter]

		cur.hot_degree -= time

	def search_prefix(self, cur_node, cur_prefix, letter):

		res = []
		cur_prefix += letter
		if cur_node and letter in cur_node.children:
			cur_node = cur_node.children[letter]
		else:
			return res, cur_prefix, None

		# dfs here
		frontier = [(cur_node, cur_prefix)]
		while frontier:
			expand, word_cur = frontier.pop()
			if expand.hot_degree:
				res.append((expand.hot_degree, word_cur))

			for kid in expand.children:
				frontier.append((expand.children[kid], word_cur + kid))

		sorted_words = list(map(lambda x: x[1], sorted(res)[:3]))
		return sorted_words, cur_prefix, cur_node

	def input(self, c):
		"""
		:type c: str
		:rtype: List[str]
		"""
		# if #, add word to trie
		if c == "#":
			self.add_word(self.prefix, 1)
			self.prefix = ""
			self.cur_node = self.root
			return []
		else:
			top_k, self.prefix, self.cur_node = self.search_prefix(self.cur_node, self.prefix, c)
			return top_k

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

def test1():
	sentences = ["i love you", "island", "ironman", "i love leetcode"]
	times = [5,3,2,2]


	autocompleteSystem = AutocompleteSystem(sentences, times)

	# print("*"*10)
	print(autocompleteSystem.input("i"))
	print(autocompleteSystem.input(" "))
	print(autocompleteSystem.input("a"))
	print(autocompleteSystem.input("#"))
	print("\n")
	print(autocompleteSystem.input("i"))
	print(autocompleteSystem.input(" "))
	print(autocompleteSystem.input("a"))
	print(autocompleteSystem.input("#"))
	print("\n")
	print(autocompleteSystem.input("i"))
	print(autocompleteSystem.input(" "))
	print(autocompleteSystem.input("a"))
	print(autocompleteSystem.input("#"))


def test2():
	sentences = ["abc", "abbc", "a"]
	times = [3, 3, 3]


	autocompleteSystem = AutocompleteSystem(sentences, times)

	# print("*"*10)
	print(autocompleteSystem.input("b"))
	print(autocompleteSystem.input("c"))
	print(autocompleteSystem.input("#"))
	print("\n")
	print(autocompleteSystem.input("b"))
	print(autocompleteSystem.input("c"))
	print(autocompleteSystem.input("#"))
	print("\n")


test1()


