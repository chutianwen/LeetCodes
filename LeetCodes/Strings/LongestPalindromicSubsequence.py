"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""
import numpy as np

class Solution(object):
    def longestPalindromeSubseqDP(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        table = np.eye(length, dtype=np.int8)

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length, 1):
                if s[j] == s[i]:
                    if j == i + 1:
                        table[i][j] = table[i][j - 1] + 1
                    else:
                        # only +2 for table[i+1][j-1], it will only grow length at s[i+1: j]
                        table[i][j] = max(table[i + 1][j - 1] + 2, table[i][j - 1], table[i + 1][j])
                else:
                    table[i][j] = max(table[i][j - 1], table[i + 1][j - 1], table[i + 1][j])
        print(table)

        return table[0][length - 1]

    def longestPalindromeSubseq(self, s):
        """
        Needs more thougths
        :param s:
        :return:
        """
        d = {}
        def f(s):
            if s not in d:
                maxL = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
                d[s] = maxL
            return d[s]
        return f(s)

res = Solution().longestPalindromeSubseq("bbbab")
print(res)