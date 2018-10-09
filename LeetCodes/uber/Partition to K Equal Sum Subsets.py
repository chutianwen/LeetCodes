'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''


class Solution:
	def canPartitionKSubsets(self, nums, k):
		target, rem = divmod(sum(nums), k)
		if rem: return False

		def search(groups):
			if not nums: return True
			v = nums.pop()
			for i, group in enumerate(groups):

				if group + v <= target:
					groups[i] += v

					if search(groups): return True
					groups[i] -= v
				if not group: break
			nums.append(v)
			return False

		nums.sort()
		if nums[-1] > target: return False
		while nums and nums[-1] == target:
			nums.pop()
			k -= 1

		return search([0] * k)


	def get_subsets(self, nums):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		if not nums:
			return []

		if len(nums) == 1:
			return [[nums[0]]]

		res = []
		for idx, num in enumerate(nums):

			subsets = self.get_subsets(nums[idx + 1:])
			res.append([num])

			for subset in subsets:
				subset_cur = [num] + subset
				res.append(subset_cur)

		return res

	def canPartitionKSubsets(self, nums, k):
		from collections import Counter
		subsets = Counter(map(sum, self.get_subsets(nums)))
		print(subsets)
		return True if k in subsets.values() else False


class Solution2:
	def canPartitionKSubsets(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""

		# this serves as action space, keep tracking of valid actions.
		visit = [0 for i in range(len(nums))]
		target= sum(nums) // k

		def DFS(k, fromindex, cursum):
			if k == 1 and cursum == target:
				return True
			if cursum == target:
				return DFS(k-1, 0, 0)
			else:
				for i in range(fromindex, len(nums)):
					# if visit[i]:
					# print("!!!!", i, visit)
					if nums[i] + cursum <= target and not visit[i]:
						visit[i] = 1
						if DFS(k, i + 1, cursum + nums[i]):
							return True
						visit[i] = 0
				return False

		if sum(nums) % k != 0 or k > sum(nums):
			return False

		return DFS(k, 0, 0)




res = Solution2().canPartitionKSubsets([1,1,1,1,1,1,1,1,1,1], 5)
print(res)

# res2 = Solution().get_subsets([1,2,3])
# for row in res2:
# 	print(row


class Solution:
	def canPartitionKSubsets(self, nums, k):

		def driver(groups, target):
			if not nums or len(nums) == 0:
				return True

			v = nums.pop()

			for idx, group in enumerate(groups):
				if group + v <= target:
					group[idx] += v
					if driver(groups, target):
						return True
					group[idx] -= v

				if not group:
					nums.append(v)
					return False

			nums.append(v)
			return False

		target, rem = divmod(sum(nums), k)
		if rem:
			return False

		nums.sort()
		if nums[-1] > target:
			return False

		num_group = k
		while nums[-1] == target:
			nums.pop()
			num_group -= 1

		return driver([0] * num_group)
