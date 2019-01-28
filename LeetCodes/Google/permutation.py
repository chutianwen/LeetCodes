def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
res = []
def permute(a, l, r):
    if l == r:
        res.append(list(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


# Driver program to test the above function
a = [1, 2, 3, 4]
permute(a, 0, len(a) - 1)
print(len(res), res)


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        res = []
        for idx, num in enumerate(nums):
            subsets = self.permute(nums[:idx] + nums[idx+1:])
            res.extend(map(lambda x: [num] + x, subsets))
        return res

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return [[]]

        res = []
        explored = set()
        for idx, num in enumerate(nums):
            if num not in explored:
                explored.add(num)
                subsets = self.permuteUnique(nums[:idx] + nums[idx+1:])
                res.extend(map(lambda x: [num] + x, subsets))
        return res

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def driver(nums):
            if not nums:
                return [[]]

            res = []
            for idx, num in enumerate(nums):
                if idx == 0 or nums[idx] != nums[idx - 1]:
                    subsets = self.permuteUnique(nums[:idx] + nums[idx+1:])
                    res.extend(map(lambda x: [num] + x, subsets))
            return res
        return driver(nums)


class Solution2(object):
    def permute(self, nums):

        res = []

        def driver(l, r):
            if l == r:
                res.append(list(nums))
            else:
                for id in range(l, r + 1):
                    nums[id], nums[l] = nums[l], nums[id]
                    driver(l + 1, r)
                    nums[id], nums[l] = nums[l], nums[id]

        driver(0, len(nums) - 1)
        return res

    def combination(self, nums, k):
        res = []

        def dfs(nums, path):
            if len(path) == k:
                res.append(path)
                return

            explored = set()
            for idx in range(len(nums)):
                if nums[idx] not in explored:
                    explored.add(nums[idx])
                    dfs(nums[idx + 1:], path + [nums[idx]])

        dfs(nums, [])
        for r in res:
            print(r)

print("Combination")
res = Solution2().combination([1,1,2,3], 2)
print(res)
