'''
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

'''

class Solution:
	def peakIndexInMountainArray(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		lo, hi = 0, len(A) - 1

		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if 0 < mid < len(A) - 1 and A[mid -1] < A[mid] and A[mid] > A[mid + 1]:
				return mid
			elif A[mid] < A[mid + 1]:
				lo = mid + 1
			elif A[mid] > A[mid + 1]:
				hi = mid - 1
			else:
				raise ValueError

		raise ValueError

res = Solution().peakIndexInMountainArray([0, 1, 2, 3, 5, 3, 2, 0])
print(res)