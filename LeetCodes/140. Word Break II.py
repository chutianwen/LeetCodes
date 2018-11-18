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

class Solution:

	def wordBreak(self, s, wordDict):
		"""
		Time complexity : O(n^3), size of recursion tree is O(n^2), each node will take O(n)
		to create a list
		Space: O(n^3)
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		word_dict = set(wordDict)
		explored = dict()
		stop = len(s)

		def dfs(start):
			if start in explored:
				return explored[start]

			if start == stop:
				return [""]

			res = []
			for split in range(start + 1, stop + 1):
				part_left = s[start: split]
				if part_left in word_dict:
					sub_res = dfs(split)
					for part_right in sub_res:
						if part_right == "":
							res.append(part_left)
						else:
							res.append(part_left + " " + part_right)

			explored[start] = res
			return res

		result = dfs(0)
		return result


class Solution2:
	def wordBreak(self, s, wordDict):
		"""
		Time: O(n^2)
		Space: O(n)
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		explored = dict()
		stop = len(s)
		words = set(wordDict)

		def dfs(start):
			if start == stop:
				return True

			for split in range(start + 1, stop + 1):
				if split in explored:
					continue

				part_left = s[start: split]
				if part_left in words and dfs(split):
					return True

			explored[start] = False
			return False

		return dfs(0)
