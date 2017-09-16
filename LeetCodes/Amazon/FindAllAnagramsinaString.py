'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        cnt = Counter(p)
        if len(s) < len(p):
            return res
        for i in range(0, len(p) - 1):
            if s[i] in cnt:
                cnt[s[i]] -= 1
        i = len(p) - 1
        while i < len(s):
            if s[i] in cnt:
                cnt[s[i]] -= 1
                if all([a == 0 for a in cnt.values()]):
                    res.append(i + 1 - len(p))
            if s[i + 1 -len(p)] in cnt:
                cnt[s[i + 1 - len(p)]] += 1
            i += 1

        return res

    def findAnagrams2(self, s, p):
        """
        Sliding window which starts from index = len(p) - 1.
        If cnts are all zeros then current window is an answer, check s[index - len(p) + 1] contained in cnts or not,
        if contained, should cnt[s[index-len(p) + 1] += 1 for checking the next window is an answer.
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ns, np, res = len(s), len(p), []
        cnt = Counter(p)  # positive count for p
        cnt.subtract(s[:np-1])  # negative count for s
        for i in range(np-1, ns):
            cnt.update({s[i]: -1})  # decrease window right
            i < np or cnt.update({s[i-np]: 1})  # increase window left
            if not any(cnt.values()):  # check all letters count 0
                res.append(i-(np-1))
        return res
res = Solution().findAnagrams("cbaebabacd", 'abc')
print(res)
