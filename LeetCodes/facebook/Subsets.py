'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
	def __init__(self):
		self.cnt = 0

	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.cnt += 1
		if not nums or len(nums) == 0:
			return [[]]

		result = []

		result_subset = self.subsets(nums[1:])
		result.extend(result_subset)
		result.extend(map(lambda subset: [nums[0]] + subset, result_subset))

		return result


class Solution2:

	def __init__(self):
		self.cnt = 0

	def subsets(self, nums):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
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

tool = Solution()
res = tool.subsets([1, 2, 3, 4])
print(res)
print(len(res))
print(tool.cnt)


import unittest

class SubsetTest(unittest.TestCase):
	"""Unit tests for isolation agents"""

	def setUp(self):
		self.nums = [1, 1, 2 ,3]

	def test_example(self):
		print(Solution().subsets(self.nums))
		print(Solution2().subsets(self.nums))

if __name__ == '__main__':
	unittest.main()
