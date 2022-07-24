'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?


'''


class Solution:
	def isSubsequenceIterator(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		t = iter(t)
		return all( letter in t for letter in s)


	def isSubsequence(self, s, t):

		from collections import defaultdict
		letter_idx = defaultdict(list)
		for idx, letter in enumerate(t):
			letter_idx[letter].append(idx)

		t_idx = -1
		for letter in s:
			if letter not in letter_idx:
				return False

			if t_idx >= letter_idx[letter][-1]:
				return False

			t_idx = self.search_closest(letter_idx[letter], t_idx)

		return True

	def search_closest(self, pool, target):
		'''
		Get the first right neighbor if existed
		:param pool:
		:param target:
		:return:
		'''
		lo, hi = 0, len(pool) - 1
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if pool[mid] == target:
				return pool[mid + 1] if mid < len(pool) - 1 else None
			elif pool[mid] > target:
				hi = mid - 1
			else:
				lo = mid + 1

		return pool[lo] if lo < len(pool) else None


res = Solution().isSubsequence("abc", "ahbgdc")
print(res)