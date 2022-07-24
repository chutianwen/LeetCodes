'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
A, E, I, O, U
'''
import re

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = 'aeiou'
        i = 0
        j = len(s) - 1
        while i < j:
            # notice to take care the edge case
            while i < len(s) and s[i].lower() not in vowels:
                i += 1
            while j >= 0 and s[j].lower() not in vowels:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
            # notice to update pointers after swapping.
            i += 1
            j -= 1
        return ''.join(s)

    def reverseVowels2(self, s):
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)

res = Solution().reverseVowels2("leEtcOde")
print(res)