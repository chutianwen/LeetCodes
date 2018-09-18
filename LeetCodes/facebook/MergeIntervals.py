# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''


class Solution(object):
	def merge1(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		res = []

		if not intervals or len(intervals) == 0:
			return res

		intervals.sort(key=lambda x: x.start)

		low, hi = intervals[0].start, intervals[0].end
		for interval in intervals[1:]:
			if interval.start <= hi:
				if hi <= interval.end:
					hi = interval.end
			else:
				res.append(Interval(low, hi))
				low, hi = interval.start, interval.end

		res.append(Interval(low, hi))
		return res


	def merge(self, intervals):
		'''
		Using last interval comparison method.
		:param intervals:
		:return:
		'''
		if not intervals or len(intervals) == 0:
			return []

		intervals.sort(key=lambda x: x.start)
		last = intervals[0]

		# handle the last one.
		res = []
		for interval in intervals:
			if last.end < interval.start:
				res.append(last)
				last = interval
			else:
				last.end = max(last.end, interval.end)
		res.append(last)
		return res


a = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
res = Solution().merge(a)
for x in res:
	print(x.start, x.end)
