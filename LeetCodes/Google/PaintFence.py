"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
"""


class Solution(object):
    def numWays(self, n, k):
        """
        Dynamic programming should think from initial cases, then get the conclusion later on.
        Paint color solutions can be consist of: # paint same color as previous step + # paint differently.
        # paint same color as previous step : requires previous step is painting differently

        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same, diff = k, k*(k-1)
        for i in range(3, n + 1):
            same, diff = diff, (same + diff)*(k-1)
        return same + diff