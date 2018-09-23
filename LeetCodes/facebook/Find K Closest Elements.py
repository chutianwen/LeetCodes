'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
'''

import math

class Solution:
	def findClosestElements(self, arr, k, x):
		"""
		:type arr: List[int]
		:type k: int
		:type x: int
		:rtype: List[int]
		"""

		lo, hi = 0, len(arr) - k - 1
		while lo <= hi:
			mid = (lo + hi) // 2
			if x - arr[mid] > arr[mid + k] - x:
				lo = mid + 1
			else:
				hi = mid - 1
			print(lo, hi, mid)
		return arr[lo: lo + k]

res = Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9], 5, 4)
print(res)
