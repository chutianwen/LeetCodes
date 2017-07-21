"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class findDisappearedNumbers:
    def findDisappearedNumbers(self, nums):
        """
        Using marker method, use current value as index to mark the pointing spot negative
        negative is a marker.
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            id = abs(num) - 1
            nums[id] = -nums[id] if nums[id] > 0 else nums[id]

        return [id + 1 for id, num in enumerate(nums) if num > 0]

res = findDisappearedNumbers().findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(res)