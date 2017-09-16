class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n *= -1
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

res = Solution().myPow(2, 3)
print(res)