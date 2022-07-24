class Solution:

	def numberToWords(self, num):
		if num == 0: return "Zero"
		words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
		         "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",
		         "Ninety"]
		return " ".join([w for w in self.to_words(num, words) if len(w) > 0])

	def to_words(self, nums, words):
		if nums >= 10 ** 9:
			return self.to_words(nums // 10 ** 9, words) + ["Billion"] + self.to_words(nums % 10 ** 9, words)
		elif nums >= 10 ** 6:
			return self.to_words(nums // 10 ** 6, words) + ["Million"] + self.to_words(nums % 10 ** 6, words)
		elif nums >= 10 ** 3:
			return self.to_words(nums // 10 ** 3, words) + ["Thousand"] + self.to_words(nums % 10 ** 3, words)
		elif nums >= 10 ** 2:
			return self.to_words(nums // 10 ** 2, words) + ["Hundred"] + self.to_words(nums % 10 ** 2, words)
		elif nums >= 20:
			return [words[(nums - 20) // 10 + 20], words[nums % 10]]
		else:
			return [words[nums]]


res = Solution().numberToWords(123)
print(res)
