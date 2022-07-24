"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""
import numpy as np
class Solution(object):
    def longestPalindromeCenterAlgorithm(self, s):
        """
        We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center,
         and there are only 2n - 1 such centers.

        You might be asking why there are 2n - 12n−1 but not nn centers?
        The reason is the center of a palindrome can be in between two letters.
        Such palindromes have even number of letters (such as \textrm{''abba''}”abba”)
        and its center are between the two \textrm{'b'}’b’s.
        :type s: str
        :rtype: str
        """
        def driver(s, left, right):
            L = left
            R = right
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1

        start = end = 0
        for i, _ in enumerate(s):
            len1 = driver(s, i, i)
            len2 = driver(s, i, i + 1)
            len_max = max(len1, len2)
            # this part is tricky, since using i not i + 1 as center, start should only be shifted by (len-1)/2
            if len_max > end - start:
                start = i - (len_max - 1)//2
                end = i + len_max//2
        return s[start: end + 1]

    def longestPalindromeDP(self, s):
        """
        DP version, using a table storing if P(i, j) is True or not
        O(n^2) time and space, updating from bottom to top
        :param s:
        :return:
        """

        length = len(s)
        table = np.eye(length, dtype=np.int8)

        max_length = -1
        res = [0, 0]

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length, 1):
                if s[j] == s[i]:
                    if j == i + 1:
                        table[i][j] = 1
                        if max_length < j - i + 1:
                            max_length = j - i + 1
                            res = [i, j]
                    elif table[i + 1][j - 1] == 1:
                        table[i][j] = 1
                        if max_length < j - i + 1:
                            max_length = j - i + 1
                            res = [i, j]
        # print(table)

        return s[res[0]:res[1] + 1]

        # res_true = np.nonzero(table)
        # # print(res_true)
        # res = np.argmax(res_true[1] - res_true[0])
        # # print(res)
        # return s[res_true[0][res]: res_true[1][res] + 1]

res = Solution().longestPalindromeDP("bababab")
print(res)