'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''

from collections import Counter
class Solution:
	def leastInterval(self, tasks, n):
		"""
		:type tasks: List[str]
		:type n: int
		:rtype: int
		"""

		if not tasks:
			return 0

		task_cnts = sorted(list(Counter(tasks).values()), reverse=True)

		empty_spots = (task_cnts[0] - 1) * n

		for cnt in task_cnts[1:]:
			empty_spots -= min(cnt, task_cnts[0] - 1)

		if empty_spots > 0:
			return empty_spots + len(tasks)
		else:
			return len(tasks)

res = Solution().leastInterval(["A","A","A","B","B","B", "C", "C"], 1)
print(res)

