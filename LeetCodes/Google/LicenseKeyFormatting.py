'''
Now you are given a string S, which represents a software license key which we would like to format. The string S is
 composed of alphanumerical characters and dashes. The dashes split the alphanumerical characters within the string into
  groups. (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are possibly
   misplaced.

We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but
still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally, all the
 lower case letters in the string must be converted to upper case.

So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need to return
the license key formatted according to the description above.

Example 1:
Input: S = "2-4A0r7-4k", K = 4

Output: "24A0-R74K"

Explanation: The string S has been split into two parts, each part has 4 characters.
Example 2:
Input: S = "2-4A0r7-4k", K = 3

Output: "24-A0R-74K"

Explanation: The string S has been split into three parts, each part has 3 characters except the first part as it could
 be sh
'''


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S:
            return ''
        contents = S.upper().replace('-', '')
        res = ''
        for id in range(0, len(contents), K):
            res += contents[id: id + K]
            # if such batch size is smaller than K, means it is last batch
            if len(contents) - id > K:
                res += '-'
        return res[::-1]

    def licenseKeyFormatting2(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        size = len(S)
        start = K if size % K == 0 else size % K
        res = S[:start]
        while start < size:
            res += '-' + S[start: start + K]
            start += K
        return res



res = Solution().licenseKeyFormatting2("2-4A0r7-4k", 3)
print(res)
