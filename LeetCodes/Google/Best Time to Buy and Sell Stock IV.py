'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

class Solution:
	def maxProfit(self, k, prices):
		"""
		:type k: int
		:type prices: List[int]
		:rtype: int
		"""
		if k == 0 or prices == []:
			return 0

		days = len(prices)
		num_transactions = k + 1  # 0th transaction up to and including kth transaction is considered.

		T = [[0 for _ in range(days)] for _ in range(num_transactions)]

		for transaction in range(1, num_transactions):
			max_diff = - prices[0]
			for day in range(1, days):
				T[transaction][day] = max(T[transaction][day - 1], prices[day] + max_diff)  # price on that day with max diff
				max_diff = max(max_diff, T[transaction - 1][day] - prices[day])  # update max_diff

		return T[-1][-1]

class Solution2:
	def maxProfit(self, k, prices):
		if k >= len(prices) // 2: return sum(sell - buy for sell, buy in zip(prices[1:], prices[:-1]) if sell - buy > 0)
		dp = [[0, -float("inf")] for _ in range(k + 1)]
		for p in prices:
			for i in range(k + 1):
				if i and dp[i - 1][1] + p > dp[i][0]: dp[i][0] = dp[i - 1][1] + p
				if dp[i][0] - p > dp[i][1]: dp[i][1] = dp[i][0] - p
		return dp[-1][0]