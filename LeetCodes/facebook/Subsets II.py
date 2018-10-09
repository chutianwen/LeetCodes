'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution:
	def __init__(self):
		self.cnt = 0

	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		nums.sort()
		return [[]] + self.get_subsets(nums)

	def get_subsets(self, nums):
		self.cnt += 1
		if not nums:
			return []

		if len(nums) == 1:
			return [[nums[0]]]

		res = []
		for idx, num in enumerate(nums):

			if idx > 0 and nums[idx] == nums[idx - 1]:
				continue
			subsets = self.get_subsets(nums[idx + 1:])
			res.append([num])

			for subset in subsets:
				subset_cur = [num] + subset
				res.append(subset_cur)

		return res

a = [1,2,2]

print(Solution().subsetsWithDup(a))