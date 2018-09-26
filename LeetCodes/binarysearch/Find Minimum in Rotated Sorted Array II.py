'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:#

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

'''

class Solution:
	def findMin(self, nums):
		"""
		1.
		---     ---
			  -
			-
		2.    -
			 -
			-    -
			    -
		:type nums: List[int]
		:rtype: int
		"""

		lo, hi = 0, len(nums) - 1

		while lo <= hi:
			mid = lo + (hi - lo) // 2
			print(mid, lo, hi)
			if nums[mid] < nums[mid - 1]:
				return nums[mid]

			if nums[mid] < nums[lo]:
				hi = mid - 1
			elif nums[mid] > nums[hi]:
				lo = mid + 1
			elif lo != hi and nums[lo] == nums[hi]:
				lo += 1
			else:
				return nums[lo]

input = [1]

res = Solution().findMin(input)
print(res)