"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the
start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k
but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

"""

class Solution(object):
    def reverseStr1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r = list(s)
        r.insert(0, '-1')
        for id in range(1, len(s), 2*k):
            r[id: id + k] = r[id + k - 1: id -1 : -1]
        return "".join(r[1:])

    def revserStr(self, s, k):

        return s[:k][::-1] + s[k: 2*k] + self.revserStr(s[2*k:], k) if s else ""

res = Solution().reverseStr("abcdefg", 2)
print(res)