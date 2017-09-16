'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''

import numpy as np

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(flags, row, col):
            flags[row, col] = True
            for delta_x, delta_y in directions:
                x, y = row + delta_x, col + delta_y
                if x < 0 or x >= m or y < 0 or y >= n or flags[x, y] or matrix[x][y] < matrix[row][col]:
                    continue
                dfs(flags, x, y)

        # construct a direction list: down, right, up, left
        # In this case, during dfs, we can simply iterating the directions.
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        m, n = len(matrix), len(matrix[0])
        flags = np.full([m, n, 2], False)
        for row in range(m):
            dfs(flags[:, :, 0], row, 0)
            dfs(flags[:, :, 1], row, n-1)
        for col in range(n):
            dfs(flags[:, :, 0], 0, col)
            dfs(flags[:, :, 1], m-1, col)
        for row in range(m):
            for col in range(n):
                if all(flags[row, col]):
                    res.append([row, col])
        return res




n = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
res = Solution().pacificAtlantic(n)
print(res)
