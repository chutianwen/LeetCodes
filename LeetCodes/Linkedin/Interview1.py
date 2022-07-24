"""
Given a sorted array with duplicates and a number, find the range in the
form of (startIndex, endIndex) of that number. For example,

find_range({0 2 3 3 3 10 10},  3) should return (2,4).
find_range({0 2 3 3 3 10 10},  6) should return (-1,-1).
The array and the number of duplicates can be large.

"""
from bisect import bisect_left, bisect_right

# [1, 3, 3, 4]
# case1: 2
# case2: 3 -> 1, insert(3, 1) => 1,(3),3,3,4
# case3: 3 -> 3, insert(3, 3) => 1, 3, 3, (3), 4
def get_range(input:list, target:int):
	if input:
		left = bisect_left(input, target)
		right = bisect_right(input, target)
		# target is not inside the input
		if input[left] != target:
			return -1, -1
		else:
			return left, right - 1
	else:
		return -1, -1


def bi_sect_left(input, target):

	lo, hi = 0, len(input) - 1
	while lo <= hi:
		mid = lo + (hi - lo) // 2
		if input[mid] == target:
			break
		elif input[mid] < target:
			lo = mid + 1
		else:
			hi = mid - 1

	if input[mid] != target:
		return (-1, -1)

	left = get_left_boundary(input, lo, mid, target)
	right = get_right_boundary(input, mid, hi, target)
	return (left, right)

def get_left_boundary(input, left, right, target):
	# [3]
	while left <= right:
		mid = left + (right - left) // 2
		if left == right and input[mid] == target:
			return mid

		if mid > 0 and input[mid] > input[mid - 1]:
			return mid

		if input[mid] == target:
			right = mid
		else:
			# lower than target
			left = mid + 1

	return right

def get_right_boudary(input, left, right, target):
	while left <= right:
		mid = left + (right - left) // 2
		if left == right and input[mid] == target:
			return mid

		if mid + 1 < len(input) and input[mid] < input[mid + 1]:
			return mid

		if input[mid] == target:
			left = mid
		else:
			right = mid - 1

	return left


