'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

class Solution:
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		if not word1 or not word2: return len(word1) or len(word2)

		pre_cache = list(range(len(word2) + 1))

		for idx, letter_w1 in enumerate(word1, 1):
			print(pre_cache)
			cur_cache = [0] * (len(word2) + 1)
			# set pos for "" in word1
			pre = cur_cache[0] = idx

			for idx_cur in range(1, len(word2) + 1):
				min_cur = min(pre + 1, pre_cache[idx_cur - 1] + int(letter_w1 != word2[idx_cur - 1]), pre_cache[idx_cur] + 1)

				pre = cur_cache[idx_cur] = min_cur

			pre_cache = cur_cache
		print(pre_cache)
		return pre_cache[-1]

res = Solution().minDistance("zoologicoarchaeologist", "zoogeologist")
print(res)