'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Seen this question in a real interview before?

'''

class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		bbbbbbbbbbbbbbbbbbb
		1234567890
		:type s: str
		:rtype: int
		"""
		max_length = 0
		max_substring = ""
		cur = ""

		for letter in s:
			if letter not in cur:
				cur += letter
				if max_length < len(cur):
					max_substring = cur
					max_length = len(cur)
			else:
				idx = cur.index(letter)
				cur = cur[idx+1:] + letter
		return max_length, max_substring

class Solution2:
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		dic, ans, start = {}, 0, 0
		for i, v in enumerate(s):
			if v in dic and start <= dic[v]:
				start = dic[v] + 1
			else:
				ans = max(ans, i - start + 1)
			dic[v] = i
		return ans

import unittest
class LongestSubstringNoRepetive(unittest.TestCase):
	def setUp(self):
		self.input = "abcabcacbasdf"

	def test_example(self):
		r, s = Solution().lengthOfLongestSubstring(self.input)
		print(r, s)

if __name__ == '__main__':
	unittest.main()
