"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

class Solution(object):
    def reverseWords1(self, s):
        """
        OOM problem
        :type s: str
        :rtype: str
        """
        try:
            cut = s.index(" ")
        except:
            return s[::-1]

        return s[:cut][::-1] + " " + self.reverseWords1(s[cut + 1:]) if s else ""

    def reverseWords(self, s):
        """
        OOM problem
        :type s: str
        :rtype: str
        """
        def driver(input):
            if not input:
                return ""
            elif len(input) == 1:
                return input[0][::-1]
            else:
                k = len(input)//2
                return driver(input[:k]) + " " + driver(input[k:])
        res = driver(s.split(" "))
        return res

res = Solution().reverseWords("Let's take LeetCode contest")
print(res)
