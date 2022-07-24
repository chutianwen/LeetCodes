"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

"""
import sys

class Solution(object):

    def maximumProduct(self, nums):
        """
        only all negative or single negative element array will produce negative product

        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums, reverse=True)

        candidate1 = nums_sorted[0] * nums_sorted[1] * nums_sorted[2]

        candidate2 = nums_sorted[0] * nums_sorted[-1] * nums_sorted[-2]

        return candidate1 if candidate1 > candidate2 else candidate2

    def maximumProductSingleScan(self, nums):

        max1, max2, max3 = [-sys.maxsize - 1] * 3
        min1, min2 = [sys.maxsize] * 2

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max1 * max2 * max3 if max1 * max2 * max3 > max1 * min1 * min2 else max1 * min1 * min2

