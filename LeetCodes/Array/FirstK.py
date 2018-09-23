import heapq

class Solution:

	def first_small_k(self, nums, k):
		'''
		Using max heap of size K. Make sure the max value of the heap is smallest among the left size - k values.
		:param nums:
		:param k:
		:return:
		'''
		if k < 1:
			return []

		res = []
		for idx, num in enumerate(nums):
			if idx < k:
				heapq.heappush(res, -num)
			elif res[0] < -num:
				heapq.heappop(res)
				heapq.heappush(res, -num)

		return list(map(lambda x: -x, res[::-1]))

	def first_large_k(self, nums, k):
		'''
		Use min heap of size K, if the smallest value maintain the biggest one in the left n - k values, then the min heap will contain all first k large values.
		:param nums:
		:param k:
		:return:
		'''
		if k < 1:
			return []

		res = []
		for idx, num in enumerate(nums):
			if idx < k:
				heapq.heappush(res, num)
			elif res[0] < num:
				heapq.heappop(res)
				heapq.heappush(res, num)

		return res

input = [4, 1, 2, 5, 1, 2, 5, 6, 3, 5, 2]

print(sorted(input))
res = Solution().first_small_k(input, 6)
print(res)

res = Solution().first_large_k(input, 6)
print(res)