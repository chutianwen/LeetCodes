'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq

class Solution(object):
	def minMeetingRooms(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: int
		"""
		interval_sort_start = sorted(intervals, key=lambda x: x.start)
		meeting_rooms = []
		for interval in interval_sort_start:
			# if no room or no room's end time early than current schedule
			if meeting_rooms and meeting_rooms[0] <= interval.start:
				heapq.heappop(meeting_rooms)
			heapq.heappush(meeting_rooms, interval.end)
		return len(meeting_rooms)

res = Solution().minMeetingRooms([Interval([7,10), Interval(2,4)])

print(res)