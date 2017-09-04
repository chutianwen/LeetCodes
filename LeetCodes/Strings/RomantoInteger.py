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
        roman_dict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        res = 0
        for id in range(len(s) - 1):
            if roman_dict[s[id]] < roman_dict[s[id + 1]]:
                res -= roman_dict[s[id]]
            else:
                res += roman_dict[s[id]]
        res += roman_dict[s[-1]]
        return res