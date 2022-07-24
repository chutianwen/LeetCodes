
def merge_range(ranges: str):
	ranges = ranges.replace(" ", "")
	ranges = ranges.split(",")

	ranges_sort = []
	for range in ranges:
		start, end = range.split(":")
		ranges_sort.append([int(start), int(end)])
	ranges_sort.sort()

	if not ranges_sort:
		return ""
	else:
		res = []
		last = ranges_sort[0]
		for range in ranges_sort[1:]:
			if last[1] < range[0] - 1:
				res.append(last)
				last = range
			else:
				last[1] = max(last[1], range[1])
		res.append(last)

		return res

res = merge_range("5:10, 1:2")
print(res)