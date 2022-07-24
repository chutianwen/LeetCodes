'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0

		valid_code = set(map(str, range(1, 27)))
		is_valid = lambda x: x in valid_code

		pre_two_step = 1 if is_valid(s[0]) else 0
		if len(s) == 1: return pre_two_step

		pre_one_step = pre_two_step if is_valid(s[1]) else 0
		if is_valid(s[:2]): pre_one_step += 1
		if len(s) == 2: return pre_one_step

		for idx, letter in enumerate(s[2:], 2):
			cur = 0

			if is_valid(s[idx - 1] + letter):
				cur += pre_two_step

			if is_valid(letter):
				cur += pre_one_step

			pre_two_step = pre_one_step
			pre_one_step = cur

		return pre_one_step

res= Solution().numDecodings("104")
print(res)


class Solution2:
	def numDecodings(self, s):
		if s[0] == "0": return 0
		dp1 = dp2 = 1
		for i in range(1, len(s)):
			if s[i] == "0" and (s[i - 1] == "0" or s[i - 1] >= "3"): return 0
			dp1, dp2 = [dp2, dp1] if s[i] == "0" else [dp2, dp2 + dp1] if "10" <= s[i -1: i + 1] <= "26" else [dp2, dp2]
		return dp2