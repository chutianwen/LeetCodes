'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

from collections import defaultdict
class Solution:
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""

		visited = defaultdict(list)

		def dfs(input, wordDict):

			if input in visited:
				return visited[input]

			if not input or len(input) == 0:
				return [""]

			res = []

			for word in wordDict:
				if input.startswith(word):
					input_next = input[len(word):]
					res_sub = dfs(input_next, wordDict)
					visited[input[len(word):]] = res_sub
					splitter = "" if input_next == "" else " "
					res.extend(map(lambda sentence: word + splitter + sentence, res_sub))

			# visited[input] = res
			return res

		sentences = dfs(s, wordDict)
		return sentences

input = "catsanddog"

wordDict = ["cat","cats","and","sand","dog"]
res = Solution().wordBreak(input, wordDict)
print(res)