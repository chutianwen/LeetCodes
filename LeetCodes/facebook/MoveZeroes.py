'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		zero_start = -1

		for idx, num in enumerate(nums):
			
			if num == 0:
				if zero_start == -1:
					zero_start = idx
				continue
			elif zero_start != -1:
				nums[idx], nums[zero_start] = nums[zero_start], nums[idx]
				zero_start += 1
		print(len(nums) - zero_start)

a = [0,1,0,3,12]
res = Solution().moveZeroes(a)
print(a)