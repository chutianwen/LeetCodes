'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and
only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''
from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        O(26*n) => O(n). Greedy, each time get the smallest letter in the string and should be the leftmost.
        leftmost is for covering possible optimal solution. abcacb
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        cnts = Counter(s)
        smallest_pos = 0
        for id, letter in enumerate(s):
            if letter < s[smallest_pos]:
                smallest_pos = id
            cnts[letter] -= 1
            if cnts[letter] == 0:
                break
        print(smallest_pos)
        print(s[smallest_pos+1:])
        return s[smallest_pos] + self.removeDuplicateLetters(s[smallest_pos+1:].replace(s[smallest_pos], ''))

res = Solution().removeDuplicateLetters("a")
print(res)