'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

import string
class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		res = ""
		ref = string.ascii_uppercase
		ref = dict(enumerate(ref))

		while n:
			res += ref[((n - 1) % 26)]
			n = (n - 1) // 26
		return res[::-1]


print(Solution().convertToTitle(26))