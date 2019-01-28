from collections import deque
def special_lotter(target):

	res = []
	sliding_win = deque()
	cur_sum = 0
	for num in range(1, target // 2 + 2):
		sliding_win.append(num)
		cur_sum += num
		while cur_sum > target:
			cur_sum -= sliding_win.popleft()
		if cur_sum == target and len(sliding_win) >= 2:
			res.append(list(sliding_win))
	return res

res = special_lotter(2)
print(res)