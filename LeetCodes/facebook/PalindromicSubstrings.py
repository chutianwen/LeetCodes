'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

'''

class Solution(object):
	def countSubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""


		cnt = 0
		limit = len(s)
		for id in range(2 * limit - 1):
			left = id // 2
			right = left + id % 2
			while left >= 0 and right < limit and s[left] == s[right]:
				cnt += 1
				left -= 1
				right += 1

		return cnt



