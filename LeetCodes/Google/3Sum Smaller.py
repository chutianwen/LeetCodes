'''
Given an array of n integers nums and a target, find the number of index triplets i, j, k with
0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
'''
import numpy as np
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def driver(start, target, cnt):
            res = []
            if cnt == 0 and target > 0:
                res.append([])

            for i in range(start, len(nums)):
                subsets = driver(i + 1, target - nums[i], cnt-1)
                for subset in subsets:
                    subset.append(i)
                res.extend(subsets)
            return res

        res = driver(0, target, 3)
        return res

    def threeSumSmaller2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def driver(start, target, cnt):
            res = 0
            if cnt == 0 and target > 0:
                return 1

            for i in range(start, len(nums)):
                sub_cnt = driver(i + 1, target - nums[i], cnt-1)
                res += sub_cnt
            return res

        res = driver(0, target, 3)
        return res

    def threeSumSmallerTwoPointer(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        cnt = 0
        for k in range(len(nums)):
            i, j = 0, k-1
            while i < j:
                cur = nums[i] + nums[j] + nums[k]
                if cur < target:
                    cnt += j - i
                    i += 1
                else:
                    j -= 1
        return cnt

nums = np.array([1, 1, -2])
res = Solution().threeSumSmaller2(nums, 2)
print(res)
# for r in res:
#     print(nums[r])
a = [1, 0, 2]
print(a.sort())