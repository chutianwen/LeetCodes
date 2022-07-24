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

import heapq


def optimize_requests(requests: list):
	if not requests:
		return 0, []

	requests = sorted(requests, key=lambda x: (x[0], -x[1]))
	print(requests)

	# end time for current plan, -total_profit current plan, path
	pq = [(requests[0][1], requests[0][0] - requests[0][1], [requests[0]])]

	for idx, item in enumerate(requests[1:], 1):
		if requests[idx][0] == requests[idx - 1][0] and requests[idx][1] <= requests[idx - 1][1]:
			continue

		start, end = item
		profit, path = 0, []
		if pq[0][0] <= start:
			_, profit_old, path_old = pq[0]
			profit, path = profit_old, path_old
			heapq.heappop(pq)

		profit += -(end - start)
		path.append((start, end))
		heapq.heappush(pq, (end, profit, path))

	for plan in pq:
		print(plan)

	print("Final answer:\n")
	_, profit, path = min(pq, key=lambda x: x[1])
	print(-profit, path)


inputs = [(1, 3), (2, 5), (10, 17), (8, 11), (16, 21), (10, 11), (16, 17), (23, 26), (25, 30)]
optimize_requests(inputs)