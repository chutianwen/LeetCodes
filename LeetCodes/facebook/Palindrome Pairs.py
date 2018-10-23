'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

'''


class Solution2(object):
	def palindromePairs(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[int]]
		"""

	def palindromePairs(self, words):
		"""
		"""
		# runtime: 776ms
		lookup = {w: i for i, w in enumerate(words)}

		res = []
		for i, w in enumerate(words):
			for j in range(len(w) + 1):
				pre, pos = w[:j], w[j:]
				if pre == pre[::-1] and pos[::-1] != w and pos[::-1] in lookup:
					res.append([lookup[pos[::-1]], i])
				if j != len(w) and pos == pos[::-1] and pre[::-1] in lookup:
					res.append([i, lookup[pre[::-1]]])
		return res

class Solution(object):
	def palindromePairs(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[int]]
		"""

		word_id = {word: idx for idx, word in enumerate(words)}

		res = []
		for word, idx in word_id.items():
			len_w = len(word)
			for split in range(len_w + 1):
				prefix, suffix = word[:split], word[split:]
				suffix_reverse = suffix[::-1]
				prefix_reverse = prefix[::-1]

				# fix prefix as middle part, find left part
				if prefix == prefix_reverse and suffix_reverse != word and suffix_reverse in word_id:
					res.append([word_id[suffix_reverse], idx])

				# keep suffix as middle part, find right part, split != len_w is for de-duplicating
				if split != len_w and suffix == suffix_reverse and prefix_reverse in word_id:
					res.append([idx, word_id[prefix_reverse]])
		return res