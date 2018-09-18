'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution(object):
	def productExceptSelf(self, nums):
		"""
		Two pass, calculate product of left and right.
		:type nums: List[int]
		:rtype: List[int]
		"""
		output = []

		p = 1
		for num in nums:
			output.append(p)
			p *= num

		p = 1
		for id in range(len(nums) - 1, -1, -1):
			output[id] *= p
			p *= nums[id]
		return output

res = Solution().productExceptSelf([1,2,3,4])
print(res)