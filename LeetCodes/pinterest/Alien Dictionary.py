'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''

from collections import deque


class Solution(object):
	def alienOrder(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""
		self.visited = {}
		self.graph = {}
		self.results = deque()
		characters = set()

		for word in words:
			for char in word:
				self.visited[char] = 0
				self.graph[char] = []
				characters.add(char)

		for i in range(len(words) - 1):
			word_1 = words[i]
			word_2 = words[i + 1]
			success = self.addEdgeBetweenTwoWords(word_1, word_2)
			if (not success):
				return ""

		for char in characters:
			success = self.topologicalSort(char)
			if not success:
				return ""

		return "".join(list(self.results))

	def topologicalSort(self, char):
		# detected cycle
		if (self.visited[char] == -1):
			return False

		# char has been visited and completed topological sort on
		if (self.visited[char] == 1):
			return True

		self.visited[char] = -1

		for neighb in self.graph[char]:
			success = self.topologicalSort(neighb)
			if (not success):
				return False

		# mark char as visited and completed topological sort
		self.visited[char] = 1

		self.results.appendleft(char)

		return True

	# an edge between var_1 and var_2 means var_1 precedes var_2
	def _addEdge(self, var_1, var_2):
		self.graph[var_1].append(var_2)

	def addEdgeBetweenTwoWords(self, word1, word2):
		for char_1, char_2 in zip(word1, word2):
			if char_1 != char_2:
				self._addEdge(char_1, char_2)
				return True

		# invalid
		# hello world cannot precedes hello. doesn't make sense
		if len(word1) > len(word2):
			return False
		return True


from collections import defaultdict, deque
class Solution(object):
	def alienOrder(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""

		graph, success = self.build_graph(words)
		if not success:
			return ""

		res, success = self.topology_sort(graph)
		return res

	def build_graph(self, words):
		graph = defaultdict(list)
	
		for word in words:
			for letter in word:
				graph[letter]

		for cur, next in zip(words, words[1:]):
			success = False
			for src, dest in zip(cur, next):
				if src != dest:
					success = True
					graph[src].append(dest)
					break

			if not success and len(cur) > len(next):
				return None, False

		return graph, True

	def topology_sort(self, graph):
		res = deque()
		explored = defaultdict(int)

		def dfs(cur):
			if explored[cur] == -1:
				return False

			if explored[cur] == 1:
				return True

			explored[cur] = -1
			if cur in graph:
				for neighbor in graph[cur]:
					flag = dfs(neighbor)
					if not flag:
						return False

			explored[cur] = 1
			res.appendleft(cur)
			return True

		for node in graph:
			flag = dfs(node)
			if not flag:
				return "", flag

		return "".join(res), True

i = ["z","x","z"]
res = Solution2().alienOrder(i)
print(res)
