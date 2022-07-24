"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
 and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of
increasing sequence.

"""


class Solution(object):
    def findSubsequences2(self, nums):
        """
        [1, 2, 3, 4] => [], [4] => [] [3] [3, 4] => [], [2], [2, 3], [2, 3, 4]
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums):
            if not nums:
                return [[]]
            res = []
            for id, num in enumerate(nums):
                subsets = helper(nums[id + 1:])
                for id, subset in enumerate(subsets):
                    subsets[id] = [num] + subsets[id]
                res.extend(subsets)
                print(res)
            return res

        def helper2(nums):
            yield []
            for id, num in enumerate(nums):
                subsets = helper(nums[id + 1:])
                for subset in subsets:
                    yield [num] + subset

        res = list(helper(nums))
        # res.remove([])
        # res = filter(lambda x: len(x) > 1, res)
        # res = list(map(list, set(map(tuple, res))))
        return res


    def findSubsequences(self, nums):

        def driver(nums):
            res = set()

            if not nums:
                return res

            for id, num in enumerate(nums):
                subsets = driver(nums[id + 1:])
                for subset in subsets:
                    if num <= subset[0]:
                        res.add((num, ) + subset)
                res.add((num, ))
            return res
        res = driver(nums)
        res = list(filter(lambda x: len(x) >= 2, map(list, res)))
        return res

    def findSubsequences3(self, nums):
        subs = {()} # subs = set; subs.add(())
        for num in nums:
            subs |= {sub + (num,)
                     for sub in subs
                     if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]


res = Solution().findSubsequences2([1, 2])
print(res)

