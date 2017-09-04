"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Notice substring is different to subsequence
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                d.pop(s[low])
                low += 1
            ret = max(i - low + 1, ret)
        return ret


res = Solution().lengthOfLongestSubstringKDistinct("bacc", 2)
print(res)
