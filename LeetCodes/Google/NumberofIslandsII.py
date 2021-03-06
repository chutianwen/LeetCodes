'''
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns
the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after
 each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or
 vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
'''


class Solution(object):
	def numIslands2(self, m, n, positions):
		parent, rank = {}, {}

		def find(x):
			if parent[x] != x:
				parent[x] = find(parent[x])
			return parent[x]

		def union(x, y):
			x, y = find(x), find(y)
			if x == y:
				return 0
			if rank[x] < rank[y]:
				x, y = y, x
			parent[y] = x
			rank[x] += rank[x] == rank[y]
			return 1

		counts, count = [], 0
		for i, j in positions:
			x = parent[x] = i, j
			rank[x] = 0
			count += 1
			for y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
				if y in parent:
					count -= union(x, y)
			counts.append(count)
		return counts


class Solution2:
	def find(self, parent, p):
		if parent[p] == p:
			return p
		parent[p] = self.find(parent, parent[p])
		return parent[p]

	def union(self, parent, rank, p1, p2):

		parent_1 = self.find(parent, p1)
		parent_2 = self.find(parent, p2)

		# print(p1, p2, "parents", parent_1, parent_2, "rank", rank[parent_1], rank[parent_2])
		if parent_1 != parent_2:
			if rank[parent_1] <= rank[parent_2]:
				parent[parent_1] = parent_2
				if rank[parent_1] == rank[parent_2]:
					rank[parent_2] += 1
			else:
				parent[parent_2] = parent_1
			return 1
		else:
			return 0

	def numIslands(self, m, n, positions):
		parent, rank = {}, {}
		cnt, res = 0, []
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

		for row, col in positions:
			p = (row, col)
			is_boundary = row < m and col < n
			if is_boundary and p not in parent:
				parent[p] = p
				rank[p] = 0
				cnt += 1
				for delta_row, delta_col in directions:
					p2 = (row + delta_row, col + delta_col)
					if p2 in parent:
						cnt -= self.union(parent, rank, p, p2)
						# print(p, parent[(1, 0)])
				res.append(cnt)

		return res


res = Solution2().numIslands(m=3, n=3, positions=[[0, 1], [1, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]])
print(res)
