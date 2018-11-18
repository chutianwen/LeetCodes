from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=4)


def calculate(x, y):
	print("{} + {} = {}".format(x, y, x + y))
	return x + y


def call_back(r):
	res = r.result()
	print("Result", res)


inputs = range(100)
inputs = zip(inputs, inputs)

for x, y in inputs:
	print(x, y)
	task = pool.submit(calculate, x, y)
	task.add_done_callback(call_back)
