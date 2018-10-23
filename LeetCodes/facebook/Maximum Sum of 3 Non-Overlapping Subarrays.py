'''
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''


class Solution:
	def maxSumOfThreeSubarrays(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""

		intervals = []

		cur_sum = 0
		for idx, num in enumerate(nums):
			cur_sum += num
			if idx >= k: cur_sum -= nums[idx - k]
			if idx >= k - 1: intervals.append(cur_sum)

		left = [0] * len(intervals)
		idx_best = 0
		for idx, sum_interval in enumerate(intervals):
			if intervals[idx_best] < sum_interval:
				idx_best = idx
			left[idx] = idx_best

		right = [0] * len(intervals)
		idx_best = len(intervals) - 1
		for idx in range(len(intervals) - 1, -1, -1):
			if intervals[idx_best] < intervals[idx]:
				idx_best = idx
			right[idx] = idx_best

		res = None

		for idx_mid in range(k, len(intervals) - k):
			idx_left, idx_right = left[idx_mid - k], right[idx_mid + k]

			cur_sum = intervals[idx_left] + intervals[idx_mid] + intervals[idx_right]

			if not res:
				res = (idx_left, idx_mid, idx_right)
			else:
				best_sum_pre = intervals[res[0]] + intervals[res[1]] + intervals[res[2]]
				if cur_sum > best_sum_pre:
					res = (idx_left, idx_mid, idx_right)
		return res

class Solution2:
	def maxSumOfThreeSubarrays(self, nums, k):
		'''
		I must admit that those start and end points of for loops are really disgusting due to problem :)
		We first calculate sum(nums[i:i + k]), sum of one single subarray, for suitable indexes and store them in "single" dictionary.
		After that from right to left we match next max subarray for each suitable subarray and store two subarrays information in "double" dictionary.
		Finally, we match next max subarray couple (double) for each suitable subarray and change result if current subarray + couple bigger than result (sm).
		Return result
		:param nums:
		:param k:
		:return:
		'''
		single, double, sm, n, cur = {}, {}, 0, len(nums), sum(nums[:k - 1])
		for i in range(k - 1, n):
			cur += nums[i]
			single[i - k + 1] = cur
			cur -= nums[i - k + 1]
		cur = n - k, single[n - k]
		for i in range(n - k, k * 2 - 1, -1):
			if single[i] >= cur[1]:
				cur = i, single[i]
			double[i - k] = cur[1] + single[i - k], i - k, cur[0]
		cur = double[n - 2 * k]
		for i in range(n - 2 * k, k - 1, -1):
			if double[i][0] >= cur[0]:
				cur = double[i]
			if single[i - k] + cur[0] >= sm:
				sm, res = single[i - k] + cur[0], [i - k, cur[1], cur[2]]
		return res