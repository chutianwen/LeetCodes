'''
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.



Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3


Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
'''

from collections import deque
class Solution:
	def shortestSubarray(self, A, K):
		"""
		This is perfectly the application of using presum.
		FAQ
		Q: How to think of such solutions?
		A: Basic idea, for array starting at every A[i], find the shortest one with sum at leat K.
		In my solution, for B[i], find the smallest j that B[j] - B[i] >= K.
		Keep this in mind for understanding two while loops.

		Q: What is the purpose of first while loop?
		A: For the current prefix sum B[i], it covers all subarray ending at A[i-1].
		We want know if there is a subarray, which starts from an index, ends at A[i-1] and has at least sum K.
		So we start to compare B[i] with the smallest prefix sum in our deque, which is B[D[0]], hoping that [i] - B[d[0]] >= K.
		So if B[i] - B[d[0]] >= K, we can update our result res = min(res, i - d.popleft()).
		The while loop helps compare one by one, until this condition isn't valid anymore.

		Q: Why we pop left in the first while loop?
		A: This the most tricky part that improve my solution to get only O(N).
		D[0] exists in our deque, it means that before B[i], we didn't find a subarray whose sum at least K.
		B[i] is the first prefix sum that valid this condition.
		In other words, A[D[0]] ~ A[i-1] is the shortest subarray starting at A[D[0]] with sum at least K.
		We have already find it for A[D[0]] and it can't be shorter, so we can drop it from our deque.

		Q: What is the purpose of second while loop?
		A: To keep B[D[i]] increasing in the deque.

		Q: Why keep the deque increase?
		A: If B[i] <= B[d.back()] and moreover we already know that i > d.back(), it means that compared with d.back(),
		B[i] can help us make the subarray length shorter and sum bigger. So no need to keep d.back() in our deque.
		:type A: List[int]
		:type K: int
		:rtype: int
		"""
		N = len(A)
		pre_sums = [0] * (N + 1)
		for idx, num in enumerate(A):
			pre_sums[idx + 1] = pre_sums[idx] + num

		d = deque()
		res = N + 1
		for idx in range(N + 1):
			while d and pre_sums[idx] - pre_sums[d[0]] >= K: res = min(res, idx - d.popleft())
			while d and pre_sums[idx] <= pre_sums[d[-1]]: d.pop()
			d.append(idx)
		return res if res <= N else -1



input = [84,-37,32,40,95]
k = 167
res = Solution().shortestSubarray(input, k)
print(res)