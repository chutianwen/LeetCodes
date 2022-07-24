'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution:
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		carry = 0
		i, j = len(a) -1, len(b) - 1
		res = ""
		while i >= 0 or j >= 0 or carry:
			cur = 0
			if i >= 0 and j >= 0:
				cur += int(a[i]) + int(b[j])
			elif i >= 0 and j < 0:
				cur += int(a[i])
			elif i < 0 and j >= 0:
				cur += int(b[j])
			cur += carry
			carry = cur // 2
			res += str(cur % 2)
			i -= 1
			j -= 1
		return res[::-1]