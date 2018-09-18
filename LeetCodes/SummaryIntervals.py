
class Solution:

	def summary(self, nums):

		res = []

		nums.append("$")

		pre = lo = hi = None

		for num in nums:
			if pre:
				if num == "$" or num > pre + 1:
					if lo == hi:
						res.append(str(lo))
					else:
						res.append("{}->{}".format(lo, hi))
					lo = hi = num
				else:
					hi = num
			else:
				lo = hi = num
			pre = num

		return res


res = Solution().summary([1,4,4,5,8,11])
print(res)
