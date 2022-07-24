'''
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.

'''

import heapq
from collections import defaultdict

class Solution(object):
	def smallestRange(self, nums):
		"""
		:type nums: List[List[int]]
		:rtype: List[int]
		"""
		# storing current num and its idx_list
		frontier, max_frontier, min_range, res = [], -float('inf'), float("inf"), []

		# idx_list: offset, limit
		off_set_lists = defaultdict(list)
		for idx, sublist in enumerate(nums):
			off_set_lists[idx] = [0, len(sublist)]
			heapq.heappush(frontier, [sublist[0], idx])
			max_frontier = max(max_frontier, sublist[0])

		while True:
			min_frontier = frontier[0][0]
			delta = max_frontier - min_frontier
			if delta < min_range:
				min_range = delta
				res[:2] = [min_frontier, max_frontier]

			_, idx_list = heapq.heappop(frontier)

			# if idx_cur reaches the upper limit gonna reach the upperlimit
			if off_set_lists[idx_list][0] == off_set_lists[idx_list][1] - 1:
				break

			# move forward the current min sublist
			off_set_lists[idx_list][0] += 1
			offset_entry_cur = off_set_lists[idx_list][0]

			max_frontier = max(max_frontier, nums[idx_list][offset_entry_cur])
			heapq.heappush(frontier, [nums[idx_list][offset_entry_cur], idx_list])

		return res

class Solution2:
	def smallestRange(self, nums):

		# num_value, idx_list, idx_entry in list, upperlimit
		frontier = [(sublist[0], idx, 0, len(sublist)) for idx, sublist in enumerate(nums)]
		heapq.heapify(frontier)

		max_frontier = max(frontier)[0]
		res = [float('-inf'), float('inf')]
		while True:
			min_frontier, idx_list, offset, upper_limit = heapq.heappop(frontier)
			if max_frontier - min_frontier < res[1] - res[0]:
				res[:2] = min_frontier, max_frontier

			if offset == upper_limit - 1:
				break

			offset += 1
			next_v = nums[idx_list][offset]
			max_frontier = max(max_frontier, next_v)
			heapq.heappush(frontier, (next_v, idx_list, offset, upper_limit))
		return res

input = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
res = Solution2().smallestRange(input)
print(res)