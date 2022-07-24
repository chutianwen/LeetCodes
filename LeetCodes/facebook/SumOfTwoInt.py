'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.

Seen this question in a real interview before?

'''

class Solution:
	def getSum(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		if not b:
			return a

		base = a ^ b
		carry = (a & b) << 1
		return self.getSum(base, carry)