'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		def get_num(i, s):
			num = 0
			while i < len(s) and s[i] not in "+-*/":
				num = num * 10 + ord(s[i]) - ord('0')
				i += 1
			return num, i

		s = s.replace(" ", "")

		numbers = []
		i = 0

		num, i = get_num(0, s)
		numbers.append(num)

		while i < len(s):
			op = s[i]
			num, i = get_num(i + 1, s)
			if op == "+":
				numbers.append(num)

			if op == "-":
				numbers.append(-num)

			if op == "*":
				numbers[-1] *= num

			if op == "/":
				numbers[-1] = numbers[-1] // num if numbers[-1] >= 0 else -(-numbers[-1] // num)


		return sum(numbers)



res = Solution().calculate("0*1*2-3/4+5*6-7*8+9/10")
print(res)