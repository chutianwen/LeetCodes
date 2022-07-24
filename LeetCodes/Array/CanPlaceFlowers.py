"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be
planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number
n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


class canPlaceFlowers:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # handle [0], [0, 1] cases
        if len(flowerbed) <= 2 and sum(flowerbed) == 0:
            n -= 1

        # handle [0, 0, 0] case
        if len(flowerbed) == 3 and sum(flowerbed) == 0:
            n -= 2

        for idx in range(len(flowerbed) - 2):
            spots = flowerbed[idx: idx + 3]
            if idx == len(flowerbed) - 3 and spots[1] == 0 and spots[2] == 0:
                flowerbed[idx + 2] = 1
                n -= 1
            elif idx == 0 and spots[idx + 1] == 0 and spots[idx] == 0:
                flowerbed[idx] = 1
                n -= 1
            elif sum(spots) == 0:
                flowerbed[idx + 1] = 1
                n -= 1
        print(flowerbed)
        return n <= 0


    def canPlaceFlowers2(self, A, N):
        for i, x in enumerate(A):
            if (not x
                and (i == 0 or A[i-1] == 0)
                and (i == len(A)-1 or A[i+1] == 0)):
                N -= 1
                A[i] = 1
        return N <= 0


res = canPlaceFlowers().canPlaceFlowers([0, 0, 1], 1)
print(res)
