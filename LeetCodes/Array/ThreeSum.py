'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the
sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
	def threeSum(self, nums):
		"""
		O(N*logN + N^2/2) => O(N^2)
		Sort array first.
		Two pointer for finding pair of -num
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		r_start = len(nums) - 1

		res = []
		for idx, num in enumerate(nums[:-2]):
			if idx > 0 and num == nums[idx - 1]:
				continue
			else:

				l, r = idx + 1, r_start
				while l < r:
					sum_cur = nums[l] + nums[r]
					if sum_cur > -num:
						r -= 1
					elif sum_cur < -num:
						l += 1
					else:
						res.append([num, nums[l], nums[r]])
						while l < r and nums[l + 1] == nums[l]:
							l += 1
						while l < r and nums[r - 1] == nums[r]:
							r -= 1
						l += 1
						r -= 1
		return res