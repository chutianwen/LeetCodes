"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for id, chr in enumerate(s):
            if chr != ' ' and (id == 0 or s[id -1] == ' '):
            # if chr != ' ' and (id == len(s) - 1 or s[id + 1] == ' '):
                cnt += 1
        return cnt