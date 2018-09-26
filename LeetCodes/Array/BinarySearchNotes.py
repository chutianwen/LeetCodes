class BinarySearchNote:

	def binary_search(self, input, target):
		'''
		Careful using mid = (lo + hi) // 2, cuz it will overflow int range, use lo + (hi - lo) // 2 instead.
		Return the position which equals target or target's closest right neighbor.
		:param input:
		:param target:
		:return:
		'''
		lo, hi = 0, len(input) - 1

		while lo <= hi:
			# mid = (lo + hi) // 2
			mid = lo + (hi - lo) // 2
			if input[mid] == target:
				return mid
			elif input[mid] < target:
				lo = mid + 1
			else:
				hi = mid - 1

		# cuz in the while loop, we always keep mid larger than target, so at then end of lo == hi
		# 'lo' points to the index which is closest one larger than target, note that if input[mid]/input[lo] < target, lo += 1
		# On the contrary, hi is the closest one smaller than target
		return lo


	def binary_search_rotated(self, input, target):

		lo, hi = 0, len(input) - 1

		while lo <= hi:
			mid = (lo + hi) // 2
			print(lo, hi)
			if input[mid] == target:
				return mid

			# decide where rotation begins
			if input[lo] <= input[mid]:
				if input[lo] <= target < input[mid]:
					hi = mid - 1
				else:
					lo = mid + 1
			else:
				if input[mid] < target <= input[hi]:
					lo = mid + 1
				else:
					hi = mid - 1
		# in this case, since at the termination loop, if input[lo] <= target < input[mid] always failed, so we cannot compare mid with target,
		return hi

input = [1,2,4,5]
print(BinarySearchNote().binary_search(input, 55))

input = [5,6,8,9,12,1,2,4]
print(BinarySearchNote().binary_search_rotated(input, 7))