"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        Time: O(2^n) Think each position as a binary variable, totally have 2^n combinations of substrings(including itself)
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        if target == 0:
            res.append([])

        for id, num in enumerate(candidates):
            subs = self.combinationSum2(candidates[id + 1:], target - num)
            for sub in subs:
                sub.insert(0, num)
            res.extend(subs)

        return res


class Solution2:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()

        def dfs(nums, cur):
            res = []
            for id, num in enumerate(nums):
                if num > cur:
                    break
                if num == cur:
                    res.append([num])
                    break
                if id > 0 and nums[id] == nums[id - 1]:
                    continue
                subs = dfs(nums[id + 1:], cur - num)
                res.extend(map(lambda x: [num] + x, subs))

            return res

        return dfs(candidates, target)

input = [-1,1,0]
t = 0
res = Solution2().combinationSum2(input, t)
print(res)
