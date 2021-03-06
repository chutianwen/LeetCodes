'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
'''

class Solution(object):

	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s = s + "$"
		def helper(stack, i):
			num = 0
			sign = '+'
			while i < len(s):
				c = s[i]
				if c == " ":
					i += 1
					continue
				if c.isdigit():
					num = 10 * num + int(c)
					i += 1
				elif c == '(':
					num, i = helper([], i+1)
				else:
					if sign == '+':
						stack.append(num)
					if sign == '-':
						stack.append(-num)
					if sign == '*':
						stack[-1] *= num
					if sign == '/':
						stack[-1] = stack[-1] // num if stack[-1] >= 0 else -(-stack[-1] // num)
					num = 0
					i += 1
					if c == ')':
						return sum(stack), i
					sign = c
			return sum(stack)

		return helper([], 0)

input = "2*(5+5*2)/3+4*(5 + (6/2+8))"

res = Solution().calculate(input)
print(res)


class Solution2:
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s += "$"

		end = len(s)
		def parse(i):
			# print(i)
			num = cur = pre = 0
			sign = "+"
			while i < end:
				letter = s[i]
				if letter == " ":
					i += 1
				elif letter.isdigit():
					cur = cur * 10 + int(letter)
					i += 1
				elif letter == "(":
					cur, i = parse(i + 1)
				else:

					# if sign == "+":
					# 	num += cur
					if sign == "-":
						cur *= -1

					if sign == "*":
						num -= pre
						cur *= pre

					if sign == "/":
						num -= pre
						cur = pre // cur if pre > 0 else -(-pre // cur)

					num += cur
					pre = cur
					cur = 0
					i += 1
					if letter == ")":
						return num, i
					sign = letter

			return num

		return parse(0)

print(Solution2().calculate(input))