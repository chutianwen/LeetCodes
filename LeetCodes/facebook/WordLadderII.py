'''

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import defaultdict, deque
from string import ascii_lowercase

class Solution:
	def findLadders(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: List[List[str]]
		"""
		ref = set(wordList)

		word_path = defaultdict(list)
		frontier = deque()
		frontier.append((beginWord, [[]]))

		while frontier:
			word_expand, parent_paths = frontier.popleft()

			for idx, letter in enumerate(word_expand):
				for new_c in ascii_lowercase:
					if new_c == letter:
						continue
					else:
						new_word = word_expand[: idx] + new_c + word_expand[idx + 1:]
						if new_word in ref and new_word:
							if new_word in word_path:
								for path in parent_paths:
									new_path = path + [new_word]
									if len(new_path) == word_path[new_word][-1]:
										word_path[new_word].append(new_path)
									else:
										break
							else:
								new_paths = map(lambda path: path + [new_word], parent_paths)
								frontier.append([new_word, new_paths])
								word_path[new_word].append(new_paths)

		return word_path[endWord]

class Solution1:
	def findLadders(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: List[List[str]]
		"""
		ref = set(wordList)

		word_path = defaultdict(list)
		word_path[beginWord] = [[beginWord]]
		frontier = deque([beginWord])

		while frontier:
			word_expand = frontier.popleft()
			parent_path = word_path[word_expand]

			for idx, letter in enumerate(word_expand):
				for new_c in ascii_lowercase:
					if new_c == letter:
						continue
					else:
						new_word = word_expand[: idx] + new_c + word_expand[idx + 1:]
						if new_word in ref:
							if new_word not in word_path:
								frontier.append(new_word)

							# since no matter when we reach the same node, the action space is still same, we can simply iterate parent path
							for path in parent_path:
								path_cur = path + [new_word]

								if new_word not in word_path or len(word_path[new_word][-1]) == len(path_cur):
									word_path[new_word].append(path_cur)
								else:
									break

		return word_path[endWord]


beginWord = "a"
endWord = "c"
wordList = ["a", "c"]

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

res = Solution().findLadders(beginWord, endWord, wordList)
print("!"*10)
print(res)