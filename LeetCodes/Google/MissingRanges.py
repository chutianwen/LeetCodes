'''
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper],
return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''


class Solution(object):
    def binarySearch(self, nums, target):

        i, j = 0, len(nums) - 1
        mid = None
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid

        if nums[mid] < target:
            return mid + 1
        else:
            return mid

    def findMissingRanges(self, nums, lower, upper):
        """
        Time: O(log(n) + n) => O(n)
        Tricky part is how [lower, upper] intersect with nums
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        if not nums or lower > nums[-1] or upper < nums[0]:
            if upper == lower:
                return ["{}".format(lower)]
            else:
                return ["{}->{}".format(lower, upper)]

        id_lower, id_upper = self.binarySearch(nums, lower), self.binarySearch(nums, upper) + 1
        nums.insert(id_lower, lower)
        nums.insert(id_upper, upper)
        pre = nums[id_lower]
        # print(nums[id_lower:id_upper + 1])
        for id in range(id_lower + 1, id_upper + 1):
            dif = nums[id] - pre
            if id == id_lower + 1:
                if dif == 1:
                    res.append(str(pre))
                if dif >= 2:
                    res.append("{}->{}".format(pre, nums[id] - 1))
            elif id == id_upper:
                # 1, 8, [9], | 9 case
                # 1, 8, [9], | 10 case
                if id < len(nums) - 1:
                    if nums[id_upper + 1] != upper:
                        if dif == 1:
                            res.append(str(upper))
                        if dif >= 2:
                            res.append("{}->{}".format(pre + 1, upper))
                    else:
                        if dif >= 2:
                            res.append("{}->{}".format(pre + 1, upper-1))
                # 1, 8, [9], | case
                if id == len(nums) - 1:
                    if dif == 1:
                        res.append(str(upper))
                    if dif >= 2:
                        res.append("{}->{}".format(pre + 1, upper))
            else:
                if dif == 2:
                    res.append(str(pre + 1))
                elif dif > 2:
                    res.append("{}->{}".format(pre + 1, nums[id] - 1))
            pre = nums[id]
        return res

    def findMissingRanges3(self, nums, lower, upper):
        """
        Time: O(log(n) + n) => O(n)
        Tricky part is how [lower, upper] intersect with nums
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        if not nums or lower > nums[-1] or upper < nums[0]:
            if upper == lower:
                return ["{}".format(lower)]
            else:
                return ["{}->{}".format(lower, upper)]

        # To make lower and upper bound consistent with the regular element in array
        lower -= 1
        upper += 1
        id_lower, id_upper = self.binarySearch(nums, lower), self.binarySearch(nums, upper) + 1
        nums.insert(id_lower, lower)
        nums.insert(id_upper, upper)
        pre = nums[id_lower]
        for num in nums[id_lower + 1:id_upper + 1]:
            dif = num - pre
            if dif == 2:
                res.append(str(pre + 1))
            if dif > 2:
                res.append("{}->{}".format(pre + 1, num - 1))
            pre = num
        return res

    def findMissingRanges2(self, A, lower, upper):
        '''
        Amazing solution!
        upper + 1 and lower - 1 is very smart idea. To make the edge case consistent with the normal cases.
        :param A:
        :param lower:
        :param upper:
        :return:
        '''
        result = []
        A.append(upper+1)
        print(A)
        pre = lower - 1
        for i in A:
            if i == pre + 2:
                result.append(str(pre + 1))
            elif i > pre + 2:
                result.append(str(pre + 1) + "->" + str(i - 1))
            pre = i
        return result

res = Solution().findMissingRanges3([0, 9], 0, 9)
print(res)

# r = Solution().binarySearch([0, 1, 3, 50, 75], 90)
# print(r)
