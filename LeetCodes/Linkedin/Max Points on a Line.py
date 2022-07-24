'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

from collections import defaultdict
from decimal import Decimal

class Solution(object):
	def maxPoints(self, points):
		"""
		:type points: List[Point]
		:rtype: int
		"""
		if not points:
			return 0

		max_cnt = 0

		for idx, p1 in enumerate(points[:-1]):
			slopes_cnt = defaultdict(int)

			cnt_overlap = 0
			for p2 in points[idx + 1:]:
				delta_x = p2.x - p1.x
				delta_y = p2.y - p1.y

				if delta_x == 0 and delta_y == 0:
					cnt_overlap += 1
					continue

				if delta_x == 0:
					slopes_cnt["k90"] += 1
				else:
					slope = Decimal(delta_y) / Decimal(delta_x)
					slopes_cnt[slope] += 1

			if not slopes_cnt.values():
				max_cnt = max(max_cnt, cnt_overlap)
			else:
				max_cnt = max(max_cnt, max(slopes_cnt.values()) + cnt_overlap)

		return max_cnt + 1

	def maxPoints2(self, points):
		"""
		:type points: List[Point]
		:rtype: int
		"""
		if len(points) == 0:
			return 0
		mm = {}
		for p in points:
			mm[(p.x, p.y)] = mm.get((p.x, p.y), 0) + 1
		P = mm.keys()
		if len(P) == 1:
			return mm[P[0]]
		maxP = 0
		for i in range(len(P) - 1):
			slopes, repCnt = {}, 1
			for j in range(i + 1, len(P)):
				dx, dy = P[i][0] - P[j][0], P[i][1] - P[j][1]
				if dx == 0:
					slope = "#"
				elif dy == 0:
					slope = 0
				else:
					slope = float(dy) / dx
				slopes[slope] = slopes.get(slope, 0) + mm[P[j]]
			maxP = max(maxP, mm[P[i]] + max(slopes.values()))
		return maxP
