'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
'''

class Solution(object):
	def findLengthOfLCIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		pre = None
		max_length = 0
		cur_length = 0

		for num in nums:
			if pre is None:
				pre = num
				max_length = cur_length = 1
			else:
				if num > pre:
					cur_length += 1
					max_length = max(max_length, cur_length)
				else:
					cur_length = 1
				pre = num

		return max_length

class Solution2:
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		unique = set(nums)
		max_len = 0
		for num in unique:
			if num - 1 not in unique:

				start, cnt = num, 0
				while start in unique:
					cnt += 1
					start += 1
				max_len = max(max_len, cnt)

		return max_len