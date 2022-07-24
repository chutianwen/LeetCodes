'''
Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c
to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
'''

import numpy as np


class Solution(object):

    def binary_search(self, x, target):
        i, j = 0, len(x) - 1
        mid = None
        while i <= j:
            mid = (i + j)//2
            if x[mid] == target:
                return mid
            elif x[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        if x[mid] < target:
            return mid + 1
        else:
            return mid

    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if not nums:
            return []

        f = lambda x: a * x ** 2 + b * x + c
        nums_new = list(map(lambda x: f(x), nums))
        if a == 0:
            if b >= 0:
                return nums_new
            else:
                return nums_new[::-1]
        else:
            center = float(-b) / (2 * a)
            cut = self.binary_search(nums, center)
            if a > 0:
                left = nums_new[:cut][::-1]
                right = nums_new[cut:]
            else:
                left = nums_new[:cut]
                right = nums_new[cut:][::-1]
            res = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            if i != len(left):
                res.extend(left[i:])
            if j != len(right):
                res.extend(right[j:])
            return res

    def sortTransformedArray_better(self, nums, a, b, c):
        '''
        The trick on processing  ---> <--- or <--- ----> array is using two pointer.
        So that iteration becomes two sorted array with same direction. Then just using merge method.
        if nums[p1] * -d > nums[p2] * -d is trick part to shortened the code, it combined two cases by using one -d
        :param nums:
        :param a:
        :param b:
        :param c:
        :return:
        '''
        nums = [x*x*a + x*b + c for x in nums]
        ret = [0] * len(nums)
        p1, p2 = 0, len(nums) - 1
        i, d = (p1, 1) if a < 0 else (p2, -1)
        while p1 <= p2:
            if nums[p1] * -d > nums[p2] * -d:
                ret[i] = nums[p1]
                p1 += 1
            else:
                ret[i] = nums[p2]
                p2 -=1
            i += d
        return ret

res = Solution().sortTransformedArray([-4, -2, 2, 4], a = -1, b = 3, c = 5)
print(res)