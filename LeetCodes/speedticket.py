


def speed_test(speed_limit, car):

	p_limit = p_car = 0

	res = []
	start = 0

	while p_limit < len(speed_limit) and p_car < len(car):

		if car[p_car][0] <= speed_limit[p_limit][0]:

			if car[p_car][1] > speed_limit[p_limit][1]:
				res.append((start, car[p_car][0]))
			start = car[p_car][0]
			p_car += 1
		else:
			if car[p_car][1] > speed_limit[p_limit][1]:
				res.append((start, speed_limit[p_limit][0]))
			start = speed_limit[p_limit][0]
			p_limit += 1
	#
	# if speed_limit[-1][1] < car[-1][1]:
	# 	res.append((start, car[-1][0]))

	print(res)

# mile, limit
speed_limit = [(50, 20), (100, 40)]
car = [(25, 10), (75, 30), (90, 50), (100, 55)]

speed_limit = [(250, 20), (500, 40), (750, 30), (1000, 60)]
car = [(150, 10), (300, 30), (400, 50), (700, 20), (1000, 40)]
speed_test(speed_limit, car)