'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
'''


class Solution(object):
	def getMoneyAmount(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [[0] * (n + 1) for _ in range(n + 1)]
		self.solve(dp, 1, n)
		self.print_path(dp, 1, n)
		return dp[1][n]

	def solve(self, dp, L, R):
		if L >= R: return 0
		if dp[L][R]: return dp[L][R]
		res_min = float("inf")
		idx_min = -1
		for i in range(L, R + 1):
			tmp = i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R))
			if res_min > tmp:
				idx_min = i
				res_min = tmp

		if L == 1 and R == 10:
			print(idx_min)
		dp[L][R] = res_min
		# dp[L][R] = min(i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R)) for i in range(L, R + 1))
		return dp[L][R]

	def print_path(self, dp, L, R):
		if L >= R: return
		for i in range(L, R + 1):
			if dp[L][R] == i + max(dp[L][i - 1], dp[i + 1][R]):
				print(L, R, i)
				if dp[L][i - 1] > dp[i + 1][R]:
					self.print_path(dp, L, i - 1)
				else:
					self.print_path(dp, i + 1, R)
				break


Solution().getMoneyAmount(3)