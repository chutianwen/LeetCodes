'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''

class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		explored = dict()

		def driver(s, p):
			if (s, p) in explored:
				return explored[(s, p)]

			if not p:
				return not s
			if not s:
				return all(map(lambda x: x == "*", p))

			if p[0] == "?" or s[0] == p[0]:
				flag = self.isMatch(s[1:], p[1:])
			elif p[0] == "*":
				flag = self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
			else:
				flag = False

			explored[(s, p)] = flag
			return flag

		return driver(s, p)

class SolutionDP(object):

	def trim(self, p):

		p = list(p)
		i, is_first = 0, True
		for letter in p:
			if letter == "*":
				if is_first:
					p[i] = letter
					is_first = False
					i += 1
			else:
				p[i] = letter
				is_first = True
				i += 1
		return "".join(p[:i])

	def isMatch(self, s, p):

		p = self.trim(p)
		m, n = len(s), len(p)
		cache = [[False for _ in range(n + 1)] for _ in range(m + 1)]
		cache[0][0] = True
		if p and p[0] == "*":
			cache[0][1] = True

		for row in range(1, m + 1):
			for col in range(1, n + 1):
				if p[col - 1] == "?" or p[col - 1] == s[row - 1]:
					cache[row][col] = cache[row-1][col-1]
				elif p[col - 1] == "*":
					cache[row][col] = cache[row-1][col] or cache[row][col -1]
		return cache[m][n]

print(SolutionDP().trim("asdf***ca**s*"))