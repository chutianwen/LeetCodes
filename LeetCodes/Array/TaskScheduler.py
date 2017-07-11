"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent
different tasks.Tasks could be done without original order. Each task could be done in one interval.
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals
that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
"""
import collections

class Solution:
    """
    Task scheduler should depend on the biggest job.
    A[][][][][][]A[][][][][][]A[][][][][][][]AXXXXXXX
    Feeling the rest jobs into slots between A, put the rest to the "X" position
    """
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        tmax = max(cnt.values())
        slots = (tmax - 1) * n
        tsum = len(tasks)
        # ['A','A','A','B','B','B'], n = 0
        # max(0, num_idles) is for n = 0 situation.
        num_idles = max(0, slots + tmax - 1 - sum(n - (n == tmax) for n in cnt.values()))
        return tsum + num_idles