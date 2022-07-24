'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''

'''
A possible solution involves a Binary Indexed Tree, used to keep track of cumulative sum of number of occurrences of numbers from 1 to 100.
For the case where 1% of numbers can be outside the range 1-100, we can calculate the median as described above and skew the result according to how many elements are less than 1 and how many elements are greater than 100.
'''
from heapq import *
class MedianFinder:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		# lo half
		self.max_h = []
		# hi half
		self.min_h = []

	def addNum(self, num):
		"""
		:type num: int
		:rtype: void
		"""
		num = float(num)
		heappush(self.max_h, -num)
		heappush(self.min_h, -heappop(self.max_h))
		if len(self.min_h) > len(self.max_h):
			heappush(self.max_h, -heappop(self.min_h))


	def findMedian(self):
		"""
		:rtype: float
		"""
		if len(self.max_h) > len(self.min_h):
			return -self.max_h[0]
		else:
			return (-self.max_h[0] + self.min_h[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()