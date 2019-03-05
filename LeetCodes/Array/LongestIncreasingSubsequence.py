"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        dp[i] represents the length of the longest increasing subsequence possible considering the array elements
        upto the i^{th}i​th index only ,by necessarily including the i^{th}ith element.
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        max_v = 1
        for i in range(1, len(nums)):
            max_cur = 0
            for j in range(0, i, 1):
                if nums[j] < nums[i]:
                    max_cur = max(max_cur, dp[j])
            dp[i] = max_cur + 1
            max_v = max(max_v, dp[i])
        print(dp)
        return max_v

class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from bisect import bisect_left
        cache = []
        for num in nums:
            pos = bisect_left(cache, num)
            if pos == len(cache):
                cache.append(num)
            else:
                cache[pos] = num
            print(cache)
        return len(cache)




res = Solution2().lengthOfLIS([11,12,13,14,15,6,7,8,101,18])
print(res)