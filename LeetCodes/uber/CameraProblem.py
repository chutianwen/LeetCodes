import random
from bisect import bisect_right, bisect_left

# import numpy as np
# print(np.arccos(0) * 180 / np.pi)


def capture_most_points(points, cover_range):

	# sort points
	points.sort()
	print("sorted: ", points)
	idx = bisect_right(points, cover_range)
	# consider the rotated case, [x:360] + [0:y]
	points_extended = points + list(map(lambda x: x + 360, points[: idx])) + [float("inf")]
	print("extended:", points_extended)
	start = 0
	cnt = 0
	max_points = 0
	result = [0, None]

	for idx, cur in enumerate(points_extended):
		delta_cur = cur - points_extended[start]
		if delta_cur <= cover_range:
			cnt += 1
		else:
			if not result[1] or idx - start > result[1] - result[0] + 1:
				result[:] = [start, idx - 1]

			max_points = max(max_points, cnt)
			# add the current point in the sliding window and chop the left
			cnt += 1
			while cur - points_extended[start] > cover_range:
				start += 1
				cnt -= 1

	if result[-1] >= len(points):
		result = [[result[0], len(points) - 1], [0, result[-1] - len(points)]]

	return result, max_points

n = 8
input = [random.uniform(0, 360) for _ in range(n)]
print(input)

test = [1, 1, 4, 5, 6, 11, 11, 11]
test2 = [1, 1, 4, 5, 6, 359, 359, 360]

res, cnt_max = capture_most_points(input, 60)
print(res, cnt_max)