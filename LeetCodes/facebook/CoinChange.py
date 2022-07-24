'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

class Solution:
	def coinChange(self, coins, amount):
		"""
		DFS with cache will still Time out of limit, BFS is very efficient in this case
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		from collections import defaultdict
		explored = defaultdict(int)

		def driver(amount):
			if amount in explored:
				return explored[amount]

			if amount == 0:
				return 0

			if amount < 0:
				return -1

			num_min = amount + 1
			for coin in coins:
				cur = driver(amount - coin)
				if cur != -1:
					num_min = min(num_min, cur)

			if num_min == amount + 1:
				explored[amount] = -1
			else:
				explored[amount] = num_min + 1

			return explored[amount]

		return driver(amount)

	def coinChangeDP(self, coins, amount):

		cache = [amount + 1] * (amount + 1)
		cache[0] = 0
		for target in range(1, amount + 1):
			for coin in coins:
				if coin <= target:
					cache[target] = min(cache[target], cache[target - coin] + 1)

		return -1 if cache[amount] == amount + 1 else cache[amount]


	def coinChange2(self, coins, amount):
		"""
		THIS IS WRONG, since amount here as global pass from top to bot, we cannot gurantee explored[amount] records the least num of coins.
		Have to do from bot to up to assin explored[amount]
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		from collections import defaultdict
		explored = defaultdict(int)

		def driver(amount, num_coin):

			# In this case, we cannot look up explored, because it's the real least num_coins globally
			# if amount in explored:
			# 	return explored[amount]

			if amount == 0:
				return num_coin

			if amount < 0:
				return -1

			num_min = float("inf")
			for coin in coins:
				cur = driver(amount - coin, num_coin + 1)
				if cur != -1:
					num_min = min(num_min, cur)

			if num_min == float("inf"):
				explored[amount] = -1
			else:
				explored[amount] = num_min

			return explored[amount]

		return driver(amount, 0)


input = [1, 2, 5]
print(Solution().coinChange(input, 11))
print(Solution().coinChangeDP(input, 11))