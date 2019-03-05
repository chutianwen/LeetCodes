from operator import truediv, add, sub, mul

class Solution:
	def judgePoint24(self, nums: 'List[int]') -> 'bool':
		if not nums:
			return False

		if len(nums) == 1:
			return abs(24 - nums[0]) <= 1e-6

		for i in range(len(nums)):
			for j in range(len(nums)):
				if i != j:
					next = [nums[k] for k in range(len(nums)) if i != k != j]
					for op in (truediv, add, sub, mul):
						if (op is add or op is mul) and j > i:
							continue
						elif op is not truediv or nums[j]:
							tmp = op(nums[i], nums[j])
							next.append(tmp)
							if self.judgePoint24(next):
								return True
							next.pop()

		return False

	def judgePoint24_path(self, inputs):

		res = []

		def dfs(nums, cur):
			if not nums:
				return

			if len(nums) == 1:
				if abs(nums[0] - 24) < 1e-6:
					print(cur)
					res.append(cur)
				return

			for i in range(len(nums)):
				for j in range(len(nums)):
					if i != j:
						nums_next = [nums[k] for k in range(len(nums)) if i != k != j]
						for op in (truediv, sub, add, mul):
							if op in (add, mul) and i < j:
								continue
							elif op is not truediv or nums[j]:
								tmp = op(nums[i], nums[j])
								nums_next.append(tmp)
								if op == add:
									sign = "+"
								elif op == sub:
									sign = "-"
								elif op == mul:
									sign = "*"
								elif op == truediv:
									sign = "/"
								expr = cur + "\t\t{} {} {}".format(nums[i], sign, nums[j])
								dfs(nums_next, expr)
								nums_next.pop()
		dfs(inputs, "")
		return res

import random
test = [5, 7, 10, 11]
print(test)
res = Solution().judgePoint24_path(test)
print(res)