'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''
class Solution:
	# @param {integer[]} numss
	# @param {integer} target
	# @return {integer}
	def search(self, nums, target):
		if not nums:
			return False

		lo, hi = 0, len(nums) - 1

		while lo <= hi:
			mid = (lo + hi) // 2
			if target == nums[mid]:
				return True

			if nums[mid] < nums[lo]:
				if nums[mid] < target <= nums[hi]:
					lo = mid + 1
				else:
					hi = mid - 1
			elif nums[mid] > nums[hi]:
				if nums[lo] <= target < nums[mid]:
					hi = mid - 1
				else:
					lo = mid + 1
			elif lo != hi and nums[lo] == nums[hi]:
				lo += 1
			else:
				if nums[mid] > target:
					hi = mid - 1
				else:
					lo = mid + 1

		return False