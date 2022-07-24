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

