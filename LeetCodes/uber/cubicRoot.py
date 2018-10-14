def cubic_root(num):

	flag_pos = 1

	if num < 0:
		num *= -1
		flag_pos = -1

	lo, hi = min(1.0, num), max(1.0, num)
	err = 1e-13
	mid = 0
	while lo <= hi:
		mid = lo + (hi - lo) / 2
		diff = num - mid ** 3
		# print(mid, diff)
		if -err < diff < err:
			break
		elif diff >= err:
			lo = mid
		else:
			hi = mid

	return mid * flag_pos

import math
value = 100
print(cubic_root(value))
print(math.pow(value, 1/3))