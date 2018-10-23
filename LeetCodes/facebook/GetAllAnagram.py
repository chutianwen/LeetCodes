

def get_all_anagram(s: str):

	from collections import Counter
	letter_cnt = Counter(s)
	num_to_go = len(s)
	res = []

	def driver(cur, num_to_go):

		if num_to_go == 0:
			res.append(cur)

		for letter in letter_cnt:
			if letter_cnt[letter] > 0:
				letter_cnt[letter] -= 1
				driver(cur + letter, num_to_go - 1)
				letter_cnt[letter] += 1

	driver("", num_to_go)
	return res

res = get_all_anagram("aabcc")
print(res)