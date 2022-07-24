from collections import defaultdict

def car_steal(elements: list):

	banned_home = defaultdict(int)
	explored_home = set()

	def dfs():

		res = 0

		for id, amt in enumerate(elements):
			if id not in explored_home and banned_home[amt] == 0:
				explored_home.add(id)
				banned_home[amt + 1] += 1
				banned_home[amt - 1] += 1
				res = max(res, amt + dfs())
				explored_home.remove(id)
				banned_home[amt + 1] -= 1
				banned_home[amt - 1] -= 1

		return res

	return dfs()


print(car_steal([1,2,3, 4, 5,6]))