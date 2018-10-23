class QuickSelect:
	def first_kth(self, nums, k):

		print("First {}th is {}\n".format(k, self.quick_select(nums, 0, len(nums) - 1, k)))

	def quick_select(self, nums, lo, hi, k):

		if lo < hi:
			partition = self.partition(nums, lo, hi)
			if partition == k - 1:
				return nums[partition]
			elif partition < k - 1:
				return self.quick_select(nums, partition + 1, hi, k)
			else:
				return self.quick_select(nums, lo, partition - 1, k)
		elif lo == hi:
			return nums[lo]

	def partition(self, nums, lo, hi):

		pivot = nums[hi]

		p1, p2 = lo, hi - 1
		while p1 <= p2:

			while p1 <= p2 and nums[p1] <= pivot:
				p1 += 1

			while p1 <= p2 and nums[p2] > pivot:
				p2 -= 1

			if p1 > p2:
				break

			nums[p1], nums[p2] = nums[p2], nums[p1]

		nums[hi], nums[p1] = nums[p1], nums[hi]
		return p1

	def quick_sort_partition(self, nums, lo, hi):
		if lo < hi:
			partition = self.partition(nums, lo, hi)
			self.quick_sort_partition(nums, lo, partition - 1)
			self.quick_sort_partition(nums, partition + 1, hi)

	def partition_with_pivot(self, nums, lo, hi, pivot):
		p1, p2 = lo, hi

		for idx in range(lo, hi + 1):
			if nums[idx] == pivot:
				nums[p1], nums[idx] = nums[idx], nums[p1]
				p1 += 1
				break

		while p1 <= p2:
			# print(p1, p2, nums[p1], nums[p2], pivot)
			while p1 <= p2 and nums[p1] <= pivot:
				p1 += 1
			while p1 <= p2 and nums[p2] > pivot:
				p2 -= 1
			if p1 > p2:
				break

			nums[p1], nums[p2] = nums[p2], nums[p1]

		nums[lo], nums[p2] = nums[p2], nums[lo]
		# print(p1, p2)
		# also only guarantee [0, p2) is <= pivot
		return p2

	def quick_sort(self, nums):
		self.quick_sort_partition(nums, 0, len(nums) - 1)

	def smaller_match_hi(self, nums_small, nums_large):

		assert (len(nums_small) == len(nums_large))

		def driver(lo, hi):
			if lo < hi:
				# this is tricky, nums_small[hi] won't work in some cases
				pivot = nums_small[(lo + hi) // 2]
				partition = self.partition_with_pivot_v2(nums_large, lo, hi, pivot)
				self.partition_with_pivot_v2(nums_small, lo, hi, nums_large[partition])
				driver(lo, partition - 1)
				driver(partition + 1, hi)

		driver(0, len(nums_small) - 1)

	def partition_with_pivot_v2(self, A, start, end, pivot):
		"""
		Use bolt to partition nuts/ Use nut to partition nuts
		Bolt and nut are swappable in the parameter

		In-place partition

		:param A: nuts or bolts, the counterpart of pivot
		:param pivot: bolt or nut
		:param start:
		:param end:
		:return: pivot
		"""
		left = start  # save for the counterpart's pivot
		i = start + 1
		while i <= end:
			if A[i] < pivot:
				left += 1
				if left != i:
					A[left], A[i] = A[i], A[left]
				i += 1
			elif A[i] == pivot:
				A[start], A[i] = A[i], A[start]
			else:
				i += 1

		# move the counterpart's pivot from start to left
		A[start], A[left] = A[left], A[start]

		# can only guarantee all pos [0, left) is <= pivot
		return left


test = [3, 1, 1, 3, 4]
print(QuickSelect().partition_with_pivot_v2(test, 0, len(test) - 1, 5))
print(test)

test = [3, 1, 1, 3, 4]
print(QuickSelect().partition_with_pivot(test, 0, len(test) - 1, 5))
print(test)

import random

nums = [random.randint(1, 100) for _ in range(10)]
# nums = [2,5,1,3,5,6,3,3]
print(nums)

QuickSelect().quick_sort(nums)
print(nums)

for _ in range(10):
	nums = [random.randint(1, 100) for _ in range(10)]
	print(nums)
	QuickSelect().first_kth(nums, 3)

print("Special case")
nums = [num for num in range(10, 0, -1)]
print(nums)
QuickSelect().first_kth(nums, 3)

print("small and high match")
nums_small = [4, 1, 1, 3, 4]
nums_large = [2, 3, 2, 5, 5]
QuickSelect().smaller_match_hi(nums_small, nums_large)
print("After matching:")
print("nums_small", nums_small)
print("nums_large", nums_large)


class Solution(object):
	def quick_select(self, nums, lo, hi, k):

		if lo < hi:
			partition = self.partition(nums, lo, hi)
			if partition == k - 1:
				return nums[partition]
			elif partition < k - 1:
				return self.quick_select(nums, partition + 1, hi, k)
			else:
				return self.quick_select(nums, lo, partition - 1, k)
		elif lo == hi:
			return nums[lo]

	def partition(self, nums, lo, hi):

		pivot = nums[hi]

		p1, p2 = lo, hi - 1
		while p1 <= p2:

			while p1 <= p2 and nums[p1] <= pivot:
				p1 += 1

			while p1 <= p2 and nums[p2] > pivot:
				p2 -= 1

			if p1 > p2:
				break

			nums[p1], nums[p2] = nums[p2], nums[p1]

		nums[hi], nums[p1] = nums[p1], nums[hi]
		return p1

	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		return self.quick_select(nums, 0, len(nums) - 1, k)
