'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""

		if not digits or len(digits) == 0:
			return []
		num_to_letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

		cur = pre = []

		for digit in digits:

			cur = []
			if pre:
				for letter in num_to_letter[digit]:
					cur.extend(map(lambda word: word + letter, pre))
			else:
				cur.extend(list(num_to_letter[digit]))

			pre = cur

		return cur

class Solution2:
	# @return a list of strings, [s1, s2]
	def letterCombinations(self, digits):
		from functools import reduce
		if '' == digits: return []
		kvmaps = {
			'2': 'abc',
			'3': 'def',
			'4': 'ghi',
			'5': 'jkl',
			'6': 'mno',
			'7': 'pqrs',
			'8': 'tuv',
			'9': 'wxyz'
		}
		return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])

res = Solution().letterCombinations("23")
print(res)