'''
220: 1 + 2 + 4 + 5 + 10 + 11 + 20 + 44 + 55 + 110  =? 284
284: 1 + 2 + 4 + 71 + 142 => 22-
'''

import math
from collections import defaultdict

class Solution:

	def amicable_pairs(self, k):
		num_sum_factor = defaultdict(float)

		# store amicable pairs in result
		res = []
		for num in range(k + 1):
			sum_factor = self.sum_factor(num)

			# -1 means num is a prime, we don't save this.
			if sum_factor != -1:
				num_sum_factor[num] = sum_factor

			# we append res only when looking back, this save us one time of calculating sum_factor twice.
			# sum_factor == num can be prime or itself is amicable number
			if sum_factor < num and sum_factor in num_sum_factor:
				# we have calculated before
				if num_sum_factor[sum_factor] == num:
					res.append([sum_factor, num])

		return res

	def sum_factor(self, num):

		# including 1 at beginning
		sum_cur, is_prime = float(1), True

		# hi can be smaller or equal then real float version of sqrt(num)
		lo, hi = 2, int(math.sqrt(num))

		for factor in range(lo, hi + 1):
			if num % factor == 0:
				is_prime = False
				sum_cur += factor + num // factor

		# ex. Given 4, hi = 2, since we have both added factor + num // factor, we need to subtract.
		if hi ** 2 == num:
			sum_cur -= hi

		return sum_cur if not is_prime else -1

res = Solution().amicable_pairs(1000000)
print(res)