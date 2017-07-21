"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Triangle(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        max_pre = triangle[-1]
        for idx in range(len(triangle) - 2, -1, -1):
            for i in range(idx + 1):
                max_pre[i] = triangle[idx][i] + min(max_pre[i], max_pre[i + 1])
            # print(max_pre)
        return max_pre[0]

nums = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
res = Triangle().minimumTotal(nums)
print(res)