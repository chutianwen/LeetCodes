def findCombinationDiffK(nums, k):

	nums.sort()
	i, j = 0, 1
	limit = len(nums)
	res = []
	while j < limit:

		diff_cur = nums[j] - nums[i]
		if diff_cur < k:
			j += 1

		elif diff_cur == k:
			res.append((nums[i], nums[j]))
			j += 1
		else:
			i += 1
			if i == j:
				j += 1
	return res

input = [2,4,15,6,1,17,19,10,20,25]
res = findCombinationDiffK(input, 2)
print(res)

