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


class Solution0(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(matrix), len(matrix[0])
        cached = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(row, col):
            if cached[row][col] != 0:
                return cached[row][col]
            res = 1
            for dir in directions:
                x, y = row + dir[0], col + dir[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[row][col]:
                    continue
                if cached[x][y] != 0:
                    res = max(res, cached[x][y] + 1)
                else:
                    res = max(res, dfs(x, y) + 1)
            cached[row][col] = res
            return res

        path_length = 0
        for row in range(m):
            for col in range(n):
                path_cur = dfs(row, col)
                path_length = max(path_length, path_cur)
        return path_length

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        explored = dict()

        def in_boundary(row, col): return 0 <= row < m and 0 <= col < n

        def dfs(row, col):
            if (row, col) in explored:
                return explored[(row, col)]

            explored[(row, col)] = 0
            max_len = 1
            for direction in directions:
                row_next, col_next = row + direction[0], col + direction[1]
                if in_boundary(row_next, col_next) and matrix[row_next][col_next] > matrix[row][col]:
                    sub_len = dfs(row_next, col_next)
                    max_len = max(max_len, 1 + sub_len)

            explored[(row, col)] = max_len
            return max_len

        res = 0
        for row in range(m):
            for col in range(n):
                res = max(res, dfs(row, col))

        return res

nums = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]
res = Solution().longestIncreasingPath(nums)
print(res)

