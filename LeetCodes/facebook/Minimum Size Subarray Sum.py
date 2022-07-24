'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''

class Solution(object):
	def minSubArrayLen(self, s, nums):
		"""
		:type s: int
		:type nums: List[int]
		:rtype: int
		"""
		min_length = sum_cur = start = 0

		for cur, num in enumerate(nums):
			sum_cur += num

			if sum_cur >= s:

				while sum_cur >= s:
					sum_cur -= nums[start]
					start += 1

				if min_length:
					min_length = min(min_length, (cur - start + 2))
				else:
					min_length = cur - start + 2
		return min_length

class Solution2(object):
	def minSubArrayLen(self, s, nums):
		"""
		:type s: int
		:type nums: List[int]
		:rtype: int
		"""
		i = j = -1
		sum_cur = 0
		min_length = 0
		while j < len(nums) - 1 or sum_cur >= s:
			if sum_cur < s:
				j += 1
				sum_cur += nums[j]
			else:
				if min_length == 0:
					min_length = j - i
				else:
					min_length = min(min_length, j - i)
				i += 1
				sum_cur -= nums[i]

		return min_length


nums = [1,2,3,4,5]
print(Solution2().minSubArrayLen(11, nums))