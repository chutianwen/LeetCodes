
def string_interweave(str1, str2):

	m, n = len(str1), len(str2)
	res = []

	def driver(i, j, cur):
		if i == m and j == n:
			res.append(cur)

		# this is exactly dfs, frontier is either valid i + 1 or j + 1
		if i < m:
			driver(i + 1, j, cur + str1[i])

		if j < n:
			driver(i, j + 1, cur + str2[j])

	driver(0, 0, "")
	print(len(res))
	print(res)

def string_interweave_bk_track(str1, str2):

	m, n = len(str1), len(str2)
	res = []

	cur_str = []

	def driver(i, j):
		if i == m and j == n:
			res.append("".join(cur_str))

		if i < m:
			cur_str.append(str1[i])
			driver(i + 1, j)
			cur_str.pop()

		if j < n:
			cur_str.append(str2[j])
			driver(i, j + 1)
			cur_str.pop()

	driver(0, 0)
	print(len(res))
	print(res)

string_interweave_bk_track("123", "45")
