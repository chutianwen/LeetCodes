
dummy_data = [4, 5, 2, 9, 1, -5, 111]
window_size = 3

# 7

def moving_average(input, window_size):

	if window_size <= len(input):

		moving_avg = []
		window_sum = sum(input[: window_size])
		moving_avg.append(window_sum / window_size)

		for id in range(window_size, len(input)):
			# chop head
			window_sum -= input[id - window_size]
			window_sum += input[id]
			moving_avg.append(window_sum / window_size)

		return moving_avg
	else:
		raise Exception("has to be longer than window size")

res = moving_average(dummy_data, window_size)
print(res)


# external source (differnet formats, semi-structured) identify ip address
# internal source

# structured ->
# semi-structured ->
# un-structured ->