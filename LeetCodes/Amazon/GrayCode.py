'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = [0]
        for i in range(n):
            # print(pow(2, i), "---", 1 << i)
            # results += [x + pow(2, i) for x in reversed(results)]
            results += [x + (1 << i) for x in reversed(results)]
        return results

    def grayCode2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = [0]
        for i in range(n):
            # print(pow(2, i), "---", 1 << i)
            results += [x + pow(2, i) for x in reversed(results)]
            # results += [x + 1 << i for x in reversed(results)]
        return results

res = Solution().grayCode(4)
res2 = Solution().grayCode2(4)
print(res)
print(res2)