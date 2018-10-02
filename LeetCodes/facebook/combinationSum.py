class Solution(object):
	def combination_to_num(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		from collections import Counter, defaultdict
		num_cnt = Counter(nums)

		num_path = defaultdict(list)
		frontier = [(0, num_cnt, [])]

		while frontier:
			cur_v, num_cnt_parent, parent_path = frontier.pop()

			for num in num_cnt_parent:
				if num_cnt_parent[num] > 0:
					num_cnt_parent_new = num_cnt_parent.copy()
					num_cnt_parent_new[num] -= 1
					v = cur_v + num
					num_path[v].append(parent_path + [num])
					frontier.append((v, num_cnt_parent_new, parent_path + [num]))

		return num_path[0]


	def combination_to_num_wrong(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		from collections import Counter, defaultdict
		num_cnt = Counter(nums)

		num_path = defaultdict(list)
		num_path[0] = [[]]
		frontier = [(0, num_cnt)]

		while frontier:
			cur_v, num_cnt_parent = frontier.pop()
			parent_path = list(num_path[cur_v])
			for num in num_cnt_parent:
				if num_cnt_parent[num] > 0:
					v = cur_v + num
					num_cnt_parent[num] -= 1

					# This should be very carefully used, and this method is only right when same node's action space is not changed.
					# Actually define a node if same should consider node meta data and also its action space, if action space are not
					# same, then we cannot simply add new future node to all parent's paths.
					# One example of [-1, 0, 1], 0 -> -1 and -1 are two paths to -1, can we add 0 for both paths to get next node( -1 )?
					for path in parent_path:
						num_path[v].append(path + [num])
					frontier.append((v, num_cnt_parent.copy()))

		return num_path[0]


a = [-1, 0, 1]
res = Solution().combination_to_num_wrong(a)
for row in res:
	print(row)