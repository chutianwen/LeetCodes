'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		if not num1 or not num2: return num1 or num2

		res = ""
		len_1, len_2 = len(num1), len(num2)

		carry = 0

		if len_1 < len_2:
			shorter, longer = num1, num2
			len_shorter, len_longer = len_1, len_2
		else:
			shorter, longer = num2, num1
			len_shorter, len_longer = len_2, len_1

		i = 1
		while i <= len_shorter or carry == 1:
			if i <= len_shorter:
				cur = ord(shorter[len_shorter - i]) + ord(longer[len_longer - i]) - 2 * ord("0") + carry
			elif i <= len_longer:
				cur = ord(longer[len_longer - i]) - ord("0") + carry
			else:
				cur = carry

			if cur >= 10:
				cur -= 10
				carry = 1
			else:
				carry = 0

			res = str(cur) + res
			i += 1

		if i <= len_longer:
			res = longer[0: len_longer - i + 1] + res
		return res