'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		(j=0 or i = mi=m or \text{B}[j-1] \leq \text{A}[i])B[j−1]≤A[i]) and
		(i = 0(i=0 or j = nj=n or \text{A}[i-1] \leq \text{B}[j])A[i−1]≤B[j])
		Means ii is perfect, we can stop searching.
		j &gt; 0j>0 and i &lt; mi<m and \text{B}[j - 1] &gt; \text{A}[i]B[j−1]>A[i]
		Means ii is too small, we must increase it.
		i &gt; 0i>0 and j &lt; nj<n and \text{A}[i - 1] &gt; \text{B}[j]A[i−1]>B[j]
		Means ii is too big, we must decrease it.
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		m, n = len(nums1), len(nums2)
		if m > n:
			nums1, nums2, m, n = nums2, nums1, n, m

		if n == 0:
			raise ValueError

		i_lo, i_hi, half_len = 0, m, (m + n + 1) // 2
		while i_lo <= i_hi:

			mid = i_lo + (i_hi - i_lo) // 2
			j = half_len - mid

			if mid > 0 and nums1[mid - 1] > nums2[j]:
				i_hi = mid - 1
			elif mid < m and nums2[j - 1] > nums1[mid]:
				i_lo = mid + 1
			else:
				if mid == 0: max_left = nums2[j - 1]
				elif j == 0: max_left = nums1[mid - 1]
				else: max_left = max(nums1[mid - 1], nums2[j - 1])

				if (m + n) & 1:
					return max_left
				if mid == m: min_right = nums2[j]
				elif j == n: min_right = nums1[mid]
				else: min_right = min(nums1[mid], nums2[j])

				return (max_left + min_right)


res = Solution().findMedianSortedArrays([1,2,4,25,222], [2,3,5,66])
print(res)