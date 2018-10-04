'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.


'''
class Solution(object):

	def __init__(self, w):
		"""
		:type w: List[int]
		"""
		self.pool = []
		pre = 0
		for weight in w:
			self.pool.append(pre + weight)
			pre = self.pool[-1]

	def pickIndex(self):
		"""
		:rtype: int
		"""
		if not self.pool:
			return -1
		print(self.pool)
		import random
		from bisect import bisect_left
		choice = random.uniform(0, self.pool[-1])
		print(choice)
		result = bisect_left(self.pool, choice)
		return result

# Your Solution object will be instantiated and called as such:
obj = Solution([1, 3])
param_1 = obj.pickIndex()
print(param_1)