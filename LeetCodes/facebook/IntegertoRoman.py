'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''


class Solution(object):
	def intToRoman(self, nums):
		"""
		:type num: int
		:rtype: str
		"""

		if nums >= 1000:
			return "M" * (nums // 1000) + self.intToRoman(nums % 1000)
		elif nums >= 900:
			return "CM" + self.intToRoman(nums - 900)
		elif nums >= 500:
			return "D" + self.intToRoman(nums - 500)
		elif nums >= 400:
			return "CD" + self.intToRoman(nums - 400)
		elif nums >= 100:
			return "C" * (nums // 100) + self.intToRoman(nums % 100)
		elif nums >= 90:
			return "XC" + self.intToRoman(nums - 90)
		elif nums >= 50:
			return "L" + self.intToRoman(nums - 50)
		elif nums >= 40:
			return "XL" + self.intToRoman(nums - 40)
		elif nums >= 10:
			return "X" * (nums // 10) + self.intToRoman(nums % 10)
		elif nums == 9:
			return "IX"
		elif nums >= 5:
			return "V" + "I" * (nums - 5)
		elif nums == 4:
			return "IV"
		else:
			return "I" * nums


res = Solution().intToRoman(1994)
print(res)