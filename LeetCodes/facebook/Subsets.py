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

class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if not nums or len(nums) == 0:
			return [[]]

		result = []

		result_subset = self.subsets(nums[1:])
		result.extend(result_subset)

		for subset in result_subset:
			result.append([nums[0]] + subset)

		return result

res = Solution().subsets([1,2 ,3, 4])
print(res)
print(len(res))