"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.


"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        1. Take care of the chrs that will be invalid after upside-down, :2,4,5,7
        2. Just use two pointer to check head and tail then move towards center
        :type num: str
        :rtype: bool
        """

        candidates = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in candidates or candidates[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True

    def isStrobogrammatic2(self, num):
        '''
        ~0: -1
        ~1: -2
        :param num:
        :return:
        '''
        # "space is important here to separate different combinations"
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)/2+1))


res = Solution().isStrobogrammatic("1")
print(res)
