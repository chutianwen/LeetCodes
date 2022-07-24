"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        else:
            return s[-1] + self.reverseString(s[:-1])

    def reverseString3(self, s):
        r = list(s)
        i, j = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

    def reverseString4(self, s):
        """
        2^ log2(N) => O(N)
        :param s:
        :return:
        """
        l = len(s)
        if l < 2:
            return s
        return self.reverseString4(s[l/2:]) + self.reverseString4(s[:l/2])

res = Solution().reverseString("hello")
print(res)