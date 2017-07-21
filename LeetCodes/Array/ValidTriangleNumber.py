"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array
that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].

"""

import collections


class triangleNumber:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_cnt = collections.Counter(nums)
        length_cnt.pop(0, None)
        sorted_length = sorted(length_cnt.keys())
        accumulated_cnt_on_length = []
        for length in sorted_length:
            if len(accumulated_cnt_on_length) == 0:
                accumulated_cnt_on_length.append(length_cnt[length])
            else:
                accumulated_cnt_on_length.append(accumulated_cnt_on_length[-1] + length_cnt[length])

        res = 0

        for mid_pointer, _ in enumerate(sorted_length):
            high_pointer = len(sorted_length) - 1
            low_pointer = mid_pointer
            while high_pointer >= mid_pointer >= low_pointer >= 0:
                while high_pointer > mid_pointer and sorted_length[high_pointer] >= \
                        (sorted_length[low_pointer] + sorted_length[mid_pointer]):
                    high_pointer -= 1

                if mid_pointer == low_pointer:
                    res += length_cnt[sorted_length[mid_pointer]] * (length_cnt[sorted_length[mid_pointer]] - 1) // 2 * \
                           (accumulated_cnt_on_length[high_pointer] - accumulated_cnt_on_length[mid_pointer])
                    res += length_cnt[sorted_length[mid_pointer]] * (length_cnt[sorted_length[mid_pointer]] - 1) * \
                           (length_cnt[sorted_length[mid_pointer]] - 2) // 6

                elif mid_pointer > low_pointer:
                    res += length_cnt[sorted_length[low_pointer]] * length_cnt[sorted_length[mid_pointer]] * \
                           (accumulated_cnt_on_length[high_pointer] - accumulated_cnt_on_length[mid_pointer])
                    res += length_cnt[sorted_length[low_pointer]] * length_cnt[sorted_length[mid_pointer]] * \
                           (length_cnt[sorted_length[mid_pointer]] - 1) // 2

                low_pointer -= 1

        return res


res = triangleNumber().triangleNumber([1, 2, 3, 4, 2, 1, 2, 45])
print(res)