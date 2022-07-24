'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		def reverse(i, j):
			while i < j:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
				j -= 1

		end = len(nums) - 1
		j = end
		while j > 0 and nums[j - 1] >= nums[j]:
			j -= 1

		if j == 0:
			reverse(0, end)
			return

		pivot = j - 1

		j = end
		while nums[j] <= nums[pivot]:
			j -= 1

		nums[pivot], nums[j] = nums[j], nums[pivot]
		reverse(pivot + 1, end)

res = Solution().nextPermutation([3,2,1])
print(res)