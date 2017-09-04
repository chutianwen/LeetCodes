"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
"""
import numpy as np
class Solution(object):
    def findTargetSumWays1(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        res = 0

        if len(nums) == 0:
            # print(S)
            if S == 0:
                return 1
            else:
                return 0
        else:
            res += self.findTargetSumWays1(nums[1:], S - nums[0])
            res += self.findTargetSumWays1(nums[1:], S + nums[0])

            return res

    def findTargetSumWays(self, nums, S):

        def helper(nums, S):
            res = 0
            if S < 0:
                return 0
            elif S == 0 and len(nums) == 0:
                return 1
            else:
                if len(nums) > 0:
                    res += helper(nums[1:], S - nums[0])
                    res += helper(nums[1:], S)
                return res

        tmp = sum(nums)
        nums = np.array(nums) * 2
        print(nums,  S + tmp)
        return helper(nums, S + tmp)


res = Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)
print(res)