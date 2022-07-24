
class Gift:
	def __init__(self, price, exchange_time=3):
		self.price = price
		self.exchange_time = exchange_time

def exchange_gift(gifts: list):
	'''

	:param gifts: N gifts sorted by price already
	:return:
	'''
	res = []
	def helper(options, cur_choices, id_person_cur, robbed_by):
		# print(len(options), cur_choices)
		# if no gifts
		if not options:
			tmp = list(map(lambda x: x.price, cur_choices))
			# print(tmp)
			res.append(tmp)
		else:
			# chose any one from the options
			for id, option in enumerate(options):
				options_left = options[:id] + options[id + 1:]

				# case robbed by others, then select one gift from pool
				if id_person_cur < len(cur_choices):
					new_choices = list(cur_choices)
					new_choices[id_person_cur] = option
				else:
					# new guy select one gift from pool
					new_choices = cur_choices + [option]

				# A new person to tak action
				helper(options_left, new_choices, len(new_choices), -1)

			# rob one from the previous:
			for id, option in enumerate(cur_choices):
				if id != id_person_cur and id != robbed_by and option.exchange_time > 0:
					option.exchange_time -= 1
					if id_person_cur < len(cur_choices):
						new_choices = list(cur_choices)
						new_choices[id_person_cur] = option
					else:
						new_choices = cur_choices + [option]
					helper(options, new_choices, id, robbed_by=id_person_cur)


	helper(gifts, [], 0, -1)
	return res

n = 7
gifts_pool = []
for price in range(1, n):
	gifts_pool.append(Gift(price))


final_res = exchange_gift(gifts_pool)
print(final_res)
a = list(filter(lambda x: n - 1 == x[5], final_res))
print(len(final_res), len(a))