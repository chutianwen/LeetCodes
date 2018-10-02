'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		"""
		Remember -1 % 4 equals 3, rather than 1
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		if numerator == 0:
			return "0"

		flag = ""
		if numerator < 0:
			if denominator < 0:
				numerator *= -1
				denominator *= -1
			else:
				numerator *= -1
				flag = "-"
		else:
			if denominator < 0:
				denominator *= -1
				flag = "-"

		res = flag + str(numerator // denominator)

		remainder = numerator % denominator

		if remainder == 0:
			return str(res)
		else:
			res += "."
			res_decimal = ""
			# now remainder is positive
			explored = dict()
			start = 0
			while remainder != 0 and remainder not in explored:
				explored[remainder] = start
				remainder *= 10
				res_decimal += str(remainder // denominator)
				remainder %= denominator
				start += 1

			if remainder == 0:
				return res + res_decimal
			else:
				start_recur = explored[remainder]
				return res + res_decimal[: start_recur] + "({})".format(res_decimal[start_recur:])

res = Solution().fractionToDecimal(-11, -442)
print(res)