"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if target < 0:
            return []
        elif target == 0:
            return [[]]
        else:
            res = []
            for id, num in enumerate(candidates):
                subs = self.combinationSum([num] + candidates[id + 1:], target - num)
                for sub in subs:
                    sub.append(num)
                res.extend(subs)

            return res

res = Solution().combinationSum([2, 3, 6, 7], 7)
print(res)