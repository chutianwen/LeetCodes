"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""

class findMaxConsecutiveOnes(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, cur = 0, 0
        max = 0
        while cur < len(nums):

            # handle ending 01111 case
            if cur == len(nums) - 1 and nums[cur] == 1:
                # handles all 1 situation and 0, 1, 1, 1 case
                if nums[pre] == 1:
                    interval = cur + 1
                else:
                    interval = cur - pre
                max = interval if interval > max else max

            if nums[cur] == 0:
                # print(cur, pre)
                # 1110 case
                if nums[pre] == 1:
                    interval = cur - pre
                else:
                    interval = cur - pre - 1
                max = interval if interval > max else max
                pre = cur
            cur += 1

        return max

    def findMaxConsecutiveOnesSimple(self, nums):
        max_l = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                max = cnt if cnt > max_l else max_l
                cnt = 0
        return max(max_l, cnt)

res = findMaxConsecutiveOnes().findMaxConsecutiveOnes([1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
print(res)