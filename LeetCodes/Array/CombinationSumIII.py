"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = self.helper(k, n, list(range(1, 10)))
        return res

    def helper(self, k, n, nums):
        res = [[]]
        if k == 0 and n == 0:
            return res
        elif k == 0 and n < 0:
            return []
        else:
            for id, num in enumerate(nums):
                sub_combinations = self.helper(k - 1, n - num, nums[id + 1:])
                for combination in sub_combinations:
                    combination.append(num)
                res.extend(sub_combinations)
            res.remove([])
            return res

res = Solution().combinationSum3(3, 9)
print(res)