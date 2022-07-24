"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different
size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the
row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as
they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the
previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""
import numpy as np

class matrixReshape(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        num_row = len(nums)
        num_col = len(nums[0])
        total_size = num_row * num_col

        if r * c != total_size:
            return nums
        else:
            ##!!! cannot use this way to initialize, since [0] * c will generate an object, change res[2][0] will
            # set number to whole column
            # res = [[0]*c] * r
            res = [[0 for _ in range(c)] for _ in range(r)]
            for idx in range(total_size):
                row_ori = idx // num_col
                col_ori = idx % num_col
                # print(row_ori, col_ori)
                row_new = idx // c
                col_new = idx % c
                # print("res[1][0]=", res[1][0])
                # print("nums[row_ori][col_ori]=", nums[row_ori][col_ori])
                # print("row_new, col_new", row_new, col_new)
                res[row_new][col_new] = nums[row_ori][col_ori]
                # print("res[row_new][col_new]=", res[row_new][col_new])
                # print("res[1][0]=", res[1][0])

        return res

    def matrixReshape2(self, nums, r, c):
        flat = sum(nums, [])
        if len(flat) != r * c:
            return nums
        tuples = zip(*([iter(flat)] * c))
        return map(list, tuples)

    def matrixReshape3(self, nums, r, c):
        try:
            res = np.reshape(nums, [r, c]).tolist()
            return res
        except Exception as e:
            print(e)
            return nums



nums =[[1,2],[4,5]]
r = 4
c = 2
res = matrixReshape().matrixReshape3(nums, r, c)
print(res)