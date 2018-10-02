'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

class Solution(object):
	def validPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		left, right = 0, len(s) - 1
		while left < right:

			if s[left] != s[right]:
				s1 = s[left: right]
				s2 = s[left + 1: right + 1]
				return s1 == s1[::-1] or s2 == s2[::-1]
			left += 1
			right -= 1
		return True

res = Solution().validPalindrome("eccer")
print(res)
