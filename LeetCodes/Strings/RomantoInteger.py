"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        ref = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        pre = None
        res = 0
        for letter in s:
            if pre and ref[letter] > pre:
                res = res - pre * 2
            res += ref[letter]
            pre = ref[letter]
        return res