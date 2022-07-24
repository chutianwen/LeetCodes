'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum
to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''
import math
from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        Thinking a graph from starting point n = 25, reaching to goal 0,
        Using BFS, from
        :type n: int
        :rtype: int
        """
        longest_edge = math.floor(math.sqrt(n))
        Q = deque([(n, [])])
        visited = set()
        cnt = 0
        while Q:
            cnt += 1
            cur, path = Q.popleft()
            for x in range(longest_edge, 0, -1):
                neighbor = cur - x**2
                if neighbor < 0:
                    continue
                elif neighbor == 0:
                    return path + [x**2]
                else:
                    if neighbor not in visited:
                        Q.append((neighbor, path + [x**2]))
                        visited.add(neighbor)

        return None

res = Solution().numSquares(12)
print(res)