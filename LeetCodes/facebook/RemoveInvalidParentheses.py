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

	def removeInvalidParentheses3(self, s):
		from collections import deque

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

		frontier = deque([(s, 0)])
		explored = set()
		res = []
		depth = -1
		while frontier:
			expand, depth_expand = frontier.popleft()
			if depth != -1 and depth_expand > depth:
				continue

			if isvalid(expand):
				if depth == -1:
					depth = depth_expand
				res.append(expand)
			else:
				for idx in range(len(expand)):
					future = expand[:idx] + expand[idx + 1:]
					if future not in explored:
						explored.add(future)
						frontier.append((future, depth_expand + 1))

		return res

	def helper(self, input, solution):
		tmp = ""
		start = 0
		for idx in solution:
			tmp += input[start:idx]
			start = idx + 1
		tmp += input[start:]
		return tmp

	def removeInvalidParenthesesWithSolution(self, s):
		from collections import deque

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

		frontier = deque([(s, [])])
		explored = set()
		res = []
		depth = -1
		while frontier:
			expand, path = frontier.popleft()
			if depth != -1 and len(path) > depth:
				continue

			if isvalid(expand):
				if depth == -1:
					depth = len(path)
				tmp = []
				for j, idx in enumerate(path):
					offset = len(list(filter(lambda x: x <= idx, path[:j])))
					tmp.append(offset + idx)
				res.append((expand, tmp))
			else:
				for idx in range(len(expand)):
					future = expand[:idx] + expand[idx + 1:]
					if future not in explored:
						explored.add(future)
						frontier.append((future, path + [idx]))

		return res

input = ")((())((()(((()("
res = Solution().removeInvalidParenthesesWithSolution(input)
for valid_str, solution in res:
	tmp = Solution().helper(input, solution)
	print(valid_str, solution, "modify as solution", tmp, valid_str == tmp)

