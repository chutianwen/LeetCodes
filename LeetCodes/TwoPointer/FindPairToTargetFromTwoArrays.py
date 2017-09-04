
import random

class FindPairToTargetFromTwoArrays:

    def FindPairToTargetFromTwoArrays(self, nums1, nums2, target):

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        print(nums1)
        print(nums2)
        p1 = 0
        p2 = len(nums2) - 1
        res = []
        while p1 < len(nums1) and p2 >= 0:
            sums = nums1[p1] + nums2[p2]
            if sums == target:
                res.append([nums1[p1], nums2[p2]])
                while p1 <= len(nums1) - 2 and nums1[p1] == nums1[p1 + 1]:
                    p1 += 1
                p1 += 1
                while p2 >= 1 and nums2[p2] == nums2[p2 - 1]:
                    p2 -= 1
                p2 -= 1
            elif sums < target:
                p1 += 1
            else:
                p2 -= 1
        return res


nums1 = [random.randint(1, 5) for _ in range(5)]
nums2 = [random.randint(1, 5) for _ in range(5)]
target = random.randint(3, 10)
print(nums1)
print(nums2)
print(target)

res = FindPairToTargetFromTwoArrays().FindPairToTargetFromTwoArrays(nums1, nums2, target)
for x in res:
    print(x)