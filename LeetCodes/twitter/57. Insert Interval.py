'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''


# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


from bisect import bisect_left, bisect_right


class Solution:
	def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
		if not intervals:
			return []

		st, ed = newInterval.start, newInterval.end
		starts = [interval.start for interval in intervals]
		ends = [interval.end for interval in intervals]
		pos_st = bisect_left(starts, st)
		pos_end = bisect_right(ends, ed)

		res = []

		last = newInterval

		if pos_st > 0:
			res.extend(intervals[: pos_st - 1])
			if intervals[pos_st].end < newInterval.start:
				res.append(intervals[pos_st])
			else:
				last.start = intervals[pos_st - 1].start
				last.end = max(intervals[pos_st - 1].end, newInterval.end)

		if intervals[pos_end].start == last.end:
			last.end = intervals[pos_end].end
			pos_end += 1

		res.append(last)
		res.extend(intervals[pos_end:])
		return res
