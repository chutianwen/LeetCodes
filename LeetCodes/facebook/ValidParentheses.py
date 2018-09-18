'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution(object):

	def isValid2(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack = []
		ref = {')': '(', ']': '[', '}': '{'}
		for letter in s:
			if letter in ref:
				if len(stack) == 0 or ref[letter] != stack[-1]:
					return False
				else:
					stack.pop()
			else:
				stack.append(letter)

		return len(stack) == 0

res = Solution().isValid("(([[[[]]]))")
print(res)