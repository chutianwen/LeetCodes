'''
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
'''

class Solution:

	def parse(self, expression):
		# make sure the last accumlated number can be counted
		expression += "$"
		stop = len(expression)
		sum_digit = cur_num = num_x = i = 0
		sign = "+"
		while i < stop:
			letter = expression[i]
			if letter.isdigit():
				cur_num = cur_num * 10 + int(letter)
				i += 1
			elif letter == " ":
				i += 1
			else:
				if sign == "-":
					cur_num *= -1

				if letter == "x":
					# to handle 0x case
					if i > 0 and expression[i - 1] == "0":
						pass
					else:
						num_x += cur_num if cur_num else 1 if sign == "+" else -1
						sign = "+"
				else:
					sum_digit += cur_num
					sign = letter
				i += 1
				cur_num = 0

		return sum_digit, num_x


	def solveEquation(self, equation):
		"""
		:type equation: str
		:rtype: str
		"""

		left, right = equation.split("=")

		left_digit, left_x = self.parse(left)
		right_digit, right_x = self.parse(right)

		delta_x_left = left_x - right_x
		delta_digit_right = right_digit - left_digit
		if delta_x_left == delta_digit_right == 0:
			return "Infinite solutions"
		elif delta_x_left == 0 and delta_digit_right != 0:
			return "No solution"
		else:
			return "x={}".format(delta_digit_right // delta_x_left)
