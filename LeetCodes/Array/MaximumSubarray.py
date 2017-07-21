"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
"""
import sys


class maxSubArray(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_cur = nums[0]
        sum_pre_min = 0 if nums[0] > 0 else nums[0]
        sum_max = nums[0]
        for num in nums[1:]:
            sum_cur += num
            sum_max = sum_cur - sum_pre_min if sum_cur - sum_pre_min > sum_max else sum_max
            sum_pre_min = sum_cur if sum_cur < sum_pre_min else sum_pre_min
            # print(sum_cur, sum_pre_min, sum_max)
        return sum_max

    def maxSubArrayBetter(self, nums):
        if not nums:
            return 0
        sum_cur = sum_max = nums[0]
        for num in nums[1:]:
            sum_cur = max(sum_cur + num, num)
            sum_max = max(sum_cur, sum_max)
        return sum_max


res = maxSubArray().maxSubArrayBetter([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
