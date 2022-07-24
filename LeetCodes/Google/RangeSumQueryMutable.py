'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

'''

import math

class NumArray(object):

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
		self.size_bucket = int(math.ceil(math.sqrt(len(nums))))
		self.bucket = [0 for _ in range(self.size_bucket)]
		for idx, num in enumerate(nums):
			self.bucket[idx // self.size_bucket] += num

	def update(self, i, val):
		"""
		:type i: int
		:type val: int
		:rtype: void
		"""
		self.bucket[i//self.size_bucket] -= self.nums[i]
		self.bucket[i//self.size_bucket] += val
		self.nums[i] = val


	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""

		res = 0
		start_bucket = i // self.size_bucket
		end_bucket = j // self.size_bucket
		if start_bucket == end_bucket:
			for idx in range(i, j + 1):
				res += self.nums[idx]
		else:
			for idx in range(i, (start_bucket + 1)*self.size_bucket):
				res += self.nums[idx]

			for idx in range(start_bucket + 1, end_bucket):
				res += self.bucket[idx]

			for idx in range(end_bucket* self.size_bucket, j + 1):
				res += self.nums[idx]
		return res



# Your NumArray object will be instantiated and called as such:
obj = NumArray([1, 3, 5])
print(obj.sumRange(0, 2))
obj.update(0, 2)
param_2 = obj.sumRange(0, 2)
print(param_2)