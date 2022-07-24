'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

'''

class Solution(object):
	def reorganizeString(self, S):
		"""
		:type S: str
		:rtype: str
		"""
		from collections import Counter

		# sorted letter -> freq
		letter_cnt = Counter(S).most_common(len(S))

		# As task scheduler, use most common letter as separator
		most_freq_letter, freq_most_letter = letter_cnt[0][0], letter_cnt[0][1]
		res = [most_freq_letter] * freq_most_letter

		cnt = 0
		for letter, freq in letter_cnt[1:]:
			for idx in range(freq):
				res[cnt % freq_most_letter] += letter
				cnt += 1

		if freq_most_letter > 1 and res[-2] == most_freq_letter:
			return ""
		else:
			return "".join(res)


res = Solution().reorganizeString("vvvvlo")
print(res)
