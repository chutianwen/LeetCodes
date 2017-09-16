'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 14, 22],
  [10, 13, 14, 16, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

import numpy as np


class Solution(object):
    def binary_search(self, nums, target):

        i, j = 0, len(nums) - 1
        mid = -1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return mid

    def searchMatrix(self, matrix, target):
        """
        O(n log m)
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        matrix = np.array(matrix)

        if matrix[0, 0] > target:
            return False
        else:
            id_row_hi = self.binary_search(matrix[:, 0], target)
            if matrix[id_row_hi, 0] > target:
                id_row_hi -= 1
            id_row_lo = self.binary_search(matrix[:id_row_hi-1, -1], target)
            if matrix[id_row_lo, -1] < target:
                id_row_lo += 1
            for id_row in range(id_row_lo, id_row_hi + 1):
                id_col = self.binary_search(matrix[id_row, :], target)
                if matrix[id_row, id_col] == target:
                    return True
            return False

    def searchMatrix2(self, matrix, target):
        """
        O(m + n)
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            # wipe out the current row
            elif matrix[i][j] < target:
                i += 1
            # wipe out the current col
            else:
                j -= 1
        return False

a = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
res = Solution().searchMatrix(a, 5)
print(res)
