'''
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.

'''


class WrongSolutionGreedy(object):
	def cherryPickup(self, grid):
		def bestpath(grid):
			N = len(grid)
			NINF = float('-inf')
			dp = [[NINF] * N for _ in range(N)]
			dp[-1][-1] = grid[-1][-1]
			for i in range(N-1, -1, -1):
				for j in range(N-1, -1, -1):
					if grid[i][j] >= 0 and (i != N-1 or j != N-1):
						dp[i][j] = max(dp[i+1][j] if i+1 < N else NINF,
						               dp[i][j+1] if j+1 < N else NINF)
						dp[i][j] += grid[i][j]

			if dp[0][0] < 0: return None
			ans = [(0, 0)]
			i = j = 0
			while i != N-1 or j != N-1:
				if j+1 == N or i+1 < N and dp[i+1][j] >= dp[i][j+1]:
					i += 1
				else:
					j += 1
				ans.append((i, j))
			return ans

		ans = 0
		path = bestpath(grid)
		if path is None: return 0

		for i, j in path:
			ans += grid[i][j]
			grid[i][j] = 0

		for i, j in bestpath(grid):
			ans += grid[i][j]

		return ans

class Solution:
	def cherryPickup(self, grid: 'List[List[int]]') -> 'int':

		n = len(grid)
		cache = [[[0] * n for _ in range(n)] for _ in range(2 * n)]

		def dp(r1, c1, c2):
			r2 = r1 + c1 - c2
			if n in (r1, c1, r2, c2) or grid[r1][c1] == -1 or grid[r2][c2] == -1:
				return float('-inf')
			elif r1 == c1 == n - 1:
				return grid[r1][c1]
			elif cache[r1][c1][c2] != 0:
				return cache[r1][c1][c2]
			else:
				res = grid[r1][c1] + (grid[r2][c2] if c1 != c2 else 0)
				res += max(dp(r1 + 1, c1, c2),
				           dp(r1, c1 + 1, c2),
				           dp(r1 + 1, c1, c2 + 1),
				           dp(r1, c1 + 1, c2 + 1))

				cache[r1][c1][c2] = res
				return res

		r = max(0, dp(0, 0, 0))
		return r