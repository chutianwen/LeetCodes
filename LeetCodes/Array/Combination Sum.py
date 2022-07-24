"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()

        def dfs(nums, target, index, path, ret):
            for i in range(index, len(nums)):
                if nums[i] > target:
                    break # deadend
                if nums[i] == target:
                    ret.append([nums[i]]+path)
                    break # found
                dfs(nums, target - nums[i], i, [nums[i]]+path, ret)

        res = []
        dfs(candidates, target, 0, [], res)
        return res


class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()

        def dfs(nums, cur):
            res = []
            for id, num in enumerate(nums):
                if num > cur:
                    break
                if num == cur:
                    res.append([num])
                    break
                if id > 0 and nums[id] == nums[id - 1]:
                    continue
                subs = dfs(nums[id:], cur - num)
                res.extend(map(lambda x: [num] + x, subs))

            return res

        return dfs(candidates, target)



res = Solution().combinationSum([2, 3, 6, 7], 7)
print(res)


# airbnb question:
# http://xkcd.com/287/

# "Fruit": 2.15,
# "Fries": 2.75,
# "Salad": 3.35,
# "Wings": 3.55,
# "Mozzarella": 4.20,
# "Plate": 5.80

# f(15.05) => [
#    ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit'],
#    [...]
# ]
menu = {
    "Fruit": 2.15,
    "Fries": 2.75,
    "Salad": 3.35,
    "Wings": 3.55,
    "Mozzarella": 4.20,
    "Plate": 5.80
}


def get_orders(budget, menu):
    assert(budget >= 0, "invalid budget")

    explored = dict()

    tolerance = 1e-10

    def dfs(budget):
        if budget in explored:
            return explored[budget]
        elif -tolerance <= budget <= tolerance:
            return [[]]
        elif budget < 0:
            return []
        else:
            res = []
            for order in menu:
                sub_combination = dfs(budget - menu[order])
                res.extend(map(lambda x: [order] + x, sub_combination))

            explored[budget] = res
            return res

    order_result = dfs(budget)
    return order_result


### test case
budgets = [15.05, 6.45, 10.01]
for budget in budgets:
    res = get_orders(budget, menu)
    for sub_res in res:
        print(sub_res)
    print("--------next budget---------\n")

