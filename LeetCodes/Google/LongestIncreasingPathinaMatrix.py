'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''
import numpy as np


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(matrix), len(matrix[0])
        cached = np.zeros([m, n], dtype='i')

<<<<<<< HEAD
        def dfs(row, col):
            '''

            :param row:
            :param col:
            :return:
            '''
            # if cached[row][col] != 0:
            #     return cached[row][col]
=======
        def dfs(cached, row, col):
            if cached[row][col] != 0:
                return cached[row][col]
>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
            res = 1
            for dir in directions:
                x, y = row + dir[0], col + dir[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[row][col]:
                    continue
<<<<<<< HEAD
                if cached[x][y] != 0:
                    res = max(res, cached[x][y] + 1)
                else:
                    res = max(res, dfs(x, y) + 1)
=======
                res = max(res, dfs(cached, x, y) + 1)
>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
            cached[row][col] = res
            return res

        path_length = 0
        for row in range(m):
            for col in range(n):
<<<<<<< HEAD
                path_cur = dfs(row, col)
=======
                path_cur = dfs(cached, row, col)
>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
                path_length = max(path_length, path_cur)
        return path_length


nums = [[7, 6, 1, 1],
        [2, 7, 6, 0],
        [1, 3, 5, 1],
        [6, 6, 3, 2]]
res = Solution().longestIncreasingPath(nums)
print(res)

