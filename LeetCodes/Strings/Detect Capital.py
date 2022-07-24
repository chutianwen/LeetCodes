"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word is None:
            return None
        if len(word) <= 1:
            return True
        else:
            if 'Z' >= word[0] >= 'A':
                isAllUpper = True
                isAllLower = True
            else:
                isAllUpper = False
                isAllLower = True
            for char in word[1:]:
                if isAllLower or isAllUpper:
                    if 'Z' >= char >= 'A':
                        isAllLower = False
                    if 'a' <= char <= 'z':
                        isAllUpper = False
                else:
                    return False
            # this is the tricky part, cannot return False directly because of the case of upper case at the end.
            return isAllLower or isAllUpper

def fun():
    pass

res = Solution().detectCapitalUse(fun())
print(res)