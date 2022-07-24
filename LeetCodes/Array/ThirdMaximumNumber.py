"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

import sys


class thirdMax(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = [-sys.maxsize - 1] * 3
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2 and num != max1:
                max3 = max2
                max2 = num
            elif num > max3 and num != max2 and num != max1:
                max3 = num
        print(max1, max2, max3)

        if max3 != -sys.maxsize - 1:
            return max3
        else:
            return max1

    def thirdMax2(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                print(num)
                if num > v[0]:
                    v = [num, v[0], v[1]]
                elif num > v[1]:
                    v = [v[0], num, v[1]]
                elif num > v[2]:
                    v = [v[0], v[1], num]
            print(v)
        return max(nums) if float('-inf') in v else v[2]


res = thirdMax().thirdMax3([1, 2, 3, 2])
print(res)
print(float('-inf') < -1)
