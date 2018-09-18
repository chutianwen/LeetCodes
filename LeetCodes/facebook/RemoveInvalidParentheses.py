'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''

class Solution(object):
	def removeInvalidParentheses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		def isValid(s):
			cnt = 0
			for letter in s:
				if letter == '(':
					cnt +=1
				elif letter == ')':
					cnt -= 1
					if cnt < 0:
						return False
			return cnt == 0

		level = {s}

		while True:
			valid = list(filter(isValid, level))
			if valid:
				return valid
			level = {s[: idx] + s[idx + 1:] for s in level for idx in range(len(s))}


	def removeInvalidParentheses2(self, s):
		def isvalid(s):
			ctr = 0
			for c in s:
				if c == '(':
					ctr += 1
				elif c == ')':
					ctr -= 1
					if ctr < 0:
						return False
			return ctr == 0

		level = {s}

		while True:
			valid = filter(isvalid, level)
			if valid:
				return list(valid)
			level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

res = Solution().removeInvalidParentheses("()())()")
for x in res:
	print(res)
