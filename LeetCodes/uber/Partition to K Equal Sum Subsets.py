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
		target, rem = divmod(sum(nums), k)
		if rem: return False

		nums.sort()
		end = len(nums) - 1
		while end >= 0:
			if nums[end] == target:
				k -= 1
				end -= 1
			else:
				break

		def DFS(k, fromindex, cursum):
			if k == 0:
				return True
			else:
				for i in range(fromindex, end + 1):
					if not visit[i] and nums[i] + cursum <= target:
						visit[i] = 1
						next_sum = cursum + nums[i]
						if next_sum == target:
							if DFS(k - 1, 0, 0): return True
						else:
							if DFS(k, i + 1, next_sum): return True
						visit[i] = 0
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


class Solution3:
	def canPartitionKSubsets(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		if not k or not nums:
			return False

		target, remain = divmod(sum(nums), k)
		if remain:
			return False

		nums.sort()
		end = len(nums) - 1
		while end >= 0:
			if nums[end] == target:
				k -= 1
				end -= 1
			else:
				break
		print(nums[:end + 1], target, k)
		visited = [False] * (end + 1)
		def dfs(k_group, cur_sum, start):
			if k_group == 0:
				return True
			else:
				for split in range(start, end + 1):
					next = cur_sum + nums[split]
					if next > target:
						break

					if not visited[split] and next <= target:
						print(start, split, next)
						visited[split] = True
						if next == target:
							if dfs(k_group - 1, 0, 0): return True
						elif next < target:
							if dfs(k_group, next, split + 1): return True

						# visited[split] = False

				return False

		return dfs(k, 0, 0)

res = Solution3().canPartitionKSubsets([1,2,3,4], 2)
print(res)
