"""
You are given a string representing an attendance record for a student. The record only contains the following
 three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two
 continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False

"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt_l = 0
        cnt_a = 0
        for char in s:
            if cnt_a > 1 or cnt_l > 2:
                return False
            if char == 'L':
                cnt_l += 1
            else:
                cnt_l = 0
                if char == 'A':
                    cnt_a += 1
        return not (cnt_a > 1 or cnt_l > 2)

res = Solution().checkRecord("LALL")
print(res)