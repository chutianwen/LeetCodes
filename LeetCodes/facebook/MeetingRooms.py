'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true

'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def canAttendMeetings(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: bool
		"""
		intervals = sorted(intervals, key=lambda x: x.start)

		pre = None
		for interval in intervals:
			if pre is None:
				pre = interval.end
			else:
				if pre > interval.start:
					return False
				else:
					pre = interval.end
		return True