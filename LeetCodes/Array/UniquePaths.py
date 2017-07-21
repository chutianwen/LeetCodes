"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""
import math
class UniquePaths(object):

    def uniquePaths(self, m, n):
        """
        straight combination problem
        DDRRDDRRDDD, #n R, #m D then C(m + n, m) is the answer
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        else:
            m -= 1
            n -= 1
            total = m + n
            return math.factorial(total)/math.factorial(m)/math.factorial(n)