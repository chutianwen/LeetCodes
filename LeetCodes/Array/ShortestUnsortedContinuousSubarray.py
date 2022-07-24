"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
 then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
class findUnsortedSubarray:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < (len(nums)-1) and nums[lo] <= nums[lo + 1]:
            lo += 1

        while hi > 0 and nums[hi] >= nums[hi -1]:
            hi -= 1

        res = 0
        if lo < hi:
            min_v, max_v = min(nums[lo: hi + 1]), max(nums[lo: hi+ 1])
            print(min_v, max_v)
            while lo >= 0 and nums[lo] > min_v:
                lo -= 1
            while hi < len(nums) and nums[hi] < max_v :
                hi += 1
            res =  hi - lo - 1
        print(lo, hi)
        return res

    def findUnsortedSubarray2(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        print(is_same)
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

res = findUnsortedSubarray().findUnsortedSubarray2([1,4,4,4,2,5,4,6,7])
print(res)