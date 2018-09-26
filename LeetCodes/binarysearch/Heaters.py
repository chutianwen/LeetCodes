'''
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

'''

class Solution:
	def findRadius(self, houses, heaters):
		"""
		:type houses: List[int]
		:type heaters: List[int]
		:rtype: int
		"""
		radius = 0
		houses.sort()
		heaters.sort()
		heaters.insert(0, float('-inf'))
		heaters.append(float('inf'))
		start = 0
		for house in houses:
			while heaters[start + 1] < house:
				start += 1

			radius = max(radius, min([house - heaters[start], heaters[start + 1] - house]))

		return radius

	def calculate_new_r(self, houses, num_heater, d):

		num_individual = 0
		sum_range = 0
		ranges = []
		pre = None
		start = houses[0]
		for house in houses:
			if pre:
				if house - d/2 <= pre + d/2:
					pass
				else:
					if start == pre:
						num_individual += 1
					else:
						if pre - start > d:
							sum_range += pre - start
						ranges.append([start, pre])
					start = house
			pre = house

		if num_heater <= num_individual:
			raise Exception("Too small radius, too many individuals")

		len_ranges = list(map(lambda x: x[1] - x[0], ranges))

		# one heater can cover
		num_small_range = sum([1 for len_range in len_ranges if len_range <= d])

		d_new = sum_range / (num_heater - num_individual - num_small_range)

		print("sum range length:\t", sum_range)
		print("ranges:\t", ranges)
		print("num individuals:{}\t, num small ranges:{}".format(num_individual, num_small_range))

		is_final = False
		if abs(d_new - d) < 1e-2:
			print("\n\n-------------------------FINAL STEP-------------------------\n\n")
			print("Iteration done, d_old:{}\t d_new:{}".format(d, d_new))
			print("Tune for edge cases")
			max_d = 0
			for len_range in len_ranges:
				num_d = len_range // d_new
				num_d_float = len_range / d_new
				if num_d_float - num_d < 0.5:
					max_d = max(max_d, len_range / num_d)

			d_new = max_d
			is_final = True

		print("old_d:\t", d)
		print("new_d:\t", d_new)
		return d_new, is_final

	def find_smallest_R(self, houses, num_heater):

		houses.append(float("inf"))
		# d_old = (houses[-1] - houses[0]) / num_heater
		d_old = 0.5
		flag_stay = True

		while flag_stay:
			try:
				d_old, _ = self.calculate_new_r(houses, num_heater, d_old)
				flag_stay = False
			except Exception as e:
				d_old *= 2

		print("\n\n-------------------------BEGIN STEP-------------------------\n\n")
		for idx in range(10):
			print("{}th iteration".format(idx))
			d_new, is_final = self.calculate_new_r(houses, num_heater, d_old)
			if is_final:
				break
			d_old = d_new
			print("\n")

	def print_house(self, houses):
		houses.remove(float("inf"))
		vis = ['-'] * houses[-1]
		for house in houses:
			vis[house - 1] = '*'
		print("   ".join(vis))
		print("   ".join(map(str, list(range(1, houses[-1] + 1)))))

houses = [1, 2, 3, 6, 8, 9, 15]
# Solution().calculate_new_r(houses, 5, 1)
Solution().find_smallest_R(houses, 4)
Solution().print_house(houses)