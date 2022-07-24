'''
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
Seen this question in a real interview before?

'''


class Solution:
	def generatePalindromes(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""

		from collections import Counter

		letter_cnt = Counter(s)

		cnt_odd = 0
		letter_odd = ""
		for letter in letter_cnt:
			# if odd
			if letter_cnt[letter] & 1:
				letter_odd = letter
				cnt_odd += 1
				if cnt_odd == 2:
					return []

			letter_cnt[letter] //= 2

		res = []
		frontier = [("", letter_cnt)]
		while frontier:
			expand, letter_cnt_paths = frontier.pop()

			is_completed = True
			for letter, cnt in letter_cnt_paths.items():
				if cnt > 0:
					letter_cnt_paths_new = letter_cnt_paths.copy()
					letter_cnt_paths_new[letter] -= 1
					frontier.append((expand + letter, letter_cnt_paths_new))
					is_completed = False
			if is_completed:
				res.append(expand + letter_odd + expand[::-1])
		return res


class Solution2:
	def generatePalindromes(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		from collections import Counter

		letter_cnt = Counter(s)

		cnt_odd = 0
		letter_odd = ""
		num_required = 0
		for letter in letter_cnt:
			# if odd
			if letter_cnt[letter] & 1:
				letter_odd = letter
				cnt_odd += 1
				if cnt_odd == 2:
					return []

			letter_cnt[letter] //= 2
			num_required += letter_cnt[letter]
		res = []


		def driver(cur, num_required):
			if num_required == 0:
				res.append(cur + letter_odd + cur[::-1])
			else:
				for path in letter_cnt:
					if letter_cnt[path] > 0:
						letter_cnt[path] -= 1
						driver(cur + path, num_required - 1)
						letter_cnt[path] += 1

		driver("")
		return res



# res = Solution().generatePalindromes("aabb")
# print(res)

res2 = Solution2().generatePalindromes("ab")
print(res2)