'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''


class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		from collections import defaultdict

		letter_freq = defaultdict(int)
		for letter in t:
			letter_freq[letter] += 1

		start = end = 0
		missing = len(t)
		i = 0
		for id, letter in enumerate(s, 1):
			if letter_freq[letter] > 0:
				missing -= 1

			letter_freq[letter] -= 1
			# fully matched
			if missing == 0:
				# if letter_freq[s[i]] == 0, means it matches
				while i < id and letter_freq[s[i]] < 0:
					letter_freq[s[i]] += 1
					i += 1

				letter_freq[s[i]] += 1
				missing += 1
				if end == 0 or id - i < end - start:
					start, end = i, id
				i += 1

		return s[start: end]

res = Solution().minWindow("ADOBECODEBANC", "ABC")
print(res)
