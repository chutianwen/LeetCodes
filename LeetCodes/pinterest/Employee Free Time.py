'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Note:

schedule and schedule[i] are lists with lengths in range [1, 50].
0 <= schedule[i].start < schedule[i].end <= 10^8.

'''


# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


class Solution(object):
	def employeeFreeTime(self, schedule):
		"""
		:type schedule: List[List[Interval]]
		:rtype: List[Interval]
		"""

		def driver(lo, hi):
			if lo < hi:
				mid = lo + (hi - lo) // 2
				# merged sub_schedule
				left = driver(lo, mid)
				right = driver(mid+1, hi)
				return merge_two_list(left, right)
			elif lo == hi:
				return schedule[lo]
			else:
				return []

		def merge_two_list(left, right):
			if not left or not right:
				return left or right

			len_l, len_r = len(left), len(right)
			p_l = p_r = 0
			last, res = None, []

			while p_l < len_l and p_r < len_r:
				if left[p_l].start < right[p_r].start:
					last = merge(last, left[p_l], res)
					p_l += 1
				else:
					last = merge(last, right[p_r], res)
					p_r += 1

			while p_l < len_l:
				last = merge(last, left[p_l], res)
				p_l += 1

			while p_r < len_r:
				last = merge(last, right[p_r], res)
				p_r += 1

			if last:
				res.append(last)
			return res

		def merge(interval_last, interval_cur, res):
			if not interval_last:
				return interval_cur
			else:
				if interval_last.end < interval_cur.start:
					res.append(interval_last)
					return interval_cur
				else:
					if interval_last.end < interval_cur.end:
						interval_last.end = interval_cur.end
					return interval_last

		merged_schedule = driver(0, len(schedule) - 1)

		result = []
		for idx, schedule in enumerate(merged_schedule):
			if idx > 0 and schedule.start > merged_schedule[idx - 1].end:
				result.append(Interval(merged_schedule[idx - 1].end, schedule.start))

		return result

from heapq import *

class Solution2:
	def employeeFreeTime(self, schedule):
		'''
		O(N
		:param schedule:
		:return:
		'''
		heap = []
		for emp in schedule:
			for iv in emp:
				heap.append((iv.start, iv.end))
		heapify(heap)

		s, e = heappop(heap)
		free = e
		res = []
		while heap:
			s, e = heappop(heap)
			if s > free:
				res.append(Interval(free, s))
				free = e
			else:
				free = max(free, e)
		return res

class Solution3(object):
	def employeeFreeTime(self, schedule):
		ans = []
		pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(schedule)]
		heapify(pq)
		anchor = min(iv.start for emp in schedule for iv in emp)
		while pq:
			t, e_id, e_jx = heapq.heappop(pq)
			if anchor < t:
				ans.append(Interval(anchor, t))
			anchor = max(anchor, schedule[e_id][e_jx].end)
			if e_jx + 1 < len(schedule[e_id]):
				heapq.heappush(pq, (schedule[e_id][e_jx + 1].start, e_id, e_jx + 1))

		return ans


schedule = [[Interval(1, 2), Interval(5, 6)], [Interval(1,3), Interval(4,10)]]
res = Solution().employeeFreeTime(schedule)

for r in res:
	print(r.start, r.end)