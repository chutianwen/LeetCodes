import itertools
import math


def judgePoint24(nums):
    if len(nums) == 1:
        return math.isclose(nums[0], 24)
    return any(judgePoint24([x] + rest)
               for a, b, *rest in itertools.permutations(nums)
               for x in {a+b, a-b, a*b, b and a/b})

res = judgePoint24([24, -1])
print(res)

