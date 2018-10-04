'''
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''

from bisect import bisect_left
class Solution:
	def maxEnvelopes(self, envelopes):
		tails = []
		for w, h in sorted(envelopes, key = lambda env : (env[0], -env[1])):
			pos = bisect_left(tails, h)
			if pos == len(tails):
				tails.append(h)
			else:
				tails[pos] = h
			print(w, h, tails)
		return len(tails)

a = [[2,4],[6,4],[6,7],[2,3]]
res = Solution().maxEnvelopes(a)
