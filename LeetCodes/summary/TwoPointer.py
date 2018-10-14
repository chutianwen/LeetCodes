def findCombinationDiffK(nums, k):

	nums.sort()
	i, j = 0, 1
	limit = len(nums)
	res = []
	while j < limit:

		diff_cur = nums[j] - nums[i]
		if diff_cur < k:
			j += 1

		elif diff_cur == k:
			res.append((nums[i], nums[j]))
			j += 1
		else:
			i += 1
			if i == j:
				j += 1
	return res

input = [2,4,15,6,1,17,19,10,20,25]
res = findCombinationDiffK(input, 2)
print(res)


class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if not p:
			return not s:

		if p[0] == "?":
			return self.isMatch(s[1:], p[1:])
		else:
			first_match = bool(s) and p[0] in {s[0], '.'}
			if len(p) >= 2 and p[1] == "*":
				return first_match and self.isMatch(s[1:], p) or self.isMatch(s[1:], p[2:])
			else:
				return first_match and self.isMatch(s[1:], p[1:])

				if not p:
			return not s
		if not s:
			return not any(map(lambda x: x != "*", p[2:]))

		first_match = bool(s) and (p[0] == s[0] or p[0] == '.')

		if len(p) >= 2 and p[1] == "*":
			return first_match and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
		else:
			return first_match and self.isMatch(s[1:], p[1:])