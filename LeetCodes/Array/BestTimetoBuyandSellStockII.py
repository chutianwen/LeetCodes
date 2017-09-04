"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions
at the same time (ie, you must sell the stock before you buy again).


"""


class Solution(object):
    def maxProfit(self, prices):
        """
        [2,4,1,9,8,11]
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        else:
            sum_p = 0
            pre = prices[0]
            for price in prices[1:]:
                sum_p = max(0, price - pre)
                pre = price
            return sum_p
