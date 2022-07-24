"""
Given a non-empty string check if it can be constructed by taking a substring of it and
appending multiple copies of the substring together. You may assume the given string consists
of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length < 2:
            return False
        else:
            for id in range(0, length//2):
                cur = s[0: id + 1]
                if length % (id + 1) != 0:
                    continue
                else:
                    num = length // (id + 1)
                    if cur * num != s:
                        continue
                    else:
                        return True
            return False

    def repeatedSubstringPattern2(self, str):

        """
        Much smarter idea, as long as repeat, even only once, (str + str)[1:-1] should contains str
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1

res = Solution().repeatedSubstringPattern("aaaaaaa")
print(res)