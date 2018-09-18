'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?


'''

import collections

class Solution(object):
	def maxSubArrayLen(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""

		num_length = collections.defaultdict(int)

		max_length = sum_cur = 0

		for id, num in enumerate(nums, 1):

			sum_cur += num

			if sum_cur not in num_length:
				num_length[sum_cur] = id

			if sum_cur == k:
				max_length = max(max_length, id)
			else:
				target = sum_cur - k
				if target in num_length:
					max_length = max(max_length, id - num_length[target])

		return max_length


res = Solution().maxSubArrayLen([-2,-1,2,1], 1)

print(res)