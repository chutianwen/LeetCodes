'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''
import collections
import string

class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		word_list_lookup = set(wordList)
		explored = {beginWord: 1}
		frontier = collections.deque()
		frontier.append(beginWord)
		while frontier:
			expand = frontier.popleft()

			for idx in range(len(expand)):
				for new_c in string.ascii_lowercase:
					if new_c == expand[idx]:
						continue
					else:
						new_word = expand[:idx] + str(new_c) + expand[idx+1:]
						if new_word in word_list_lookup and new_word not in explored:
							explored[new_word] = explored[expand] + 1
							if new_word == endWord:
								return explored[new_word]
							frontier.append(new_word)

		return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

res = Solution().ladderLength(beginWord, endWord, wordList)
print(res)