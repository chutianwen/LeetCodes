'''
输入为一个大小为4的整型数组，每个整数范围1-9。判断能不能通过+，-，*， /, () 五种操作使的操作完结果是二十四。
只需判断可不可行 true/false比如，输入是 4，1，8，7 ， 返回真，因为  (8-4)*(7-1) 等于二十四。
这里数组里元素的顺序可以随意变换。又比如，输入是1，1，1，1 返回假，因为不能生成二十四。”
'''

<<<<<<< HEAD
import collections
import operator

class Solution:
    def permutation(self, nums):
        '''
        fun(nums) = [num[i] + fun(num[:i] + num[i+1:]) for i in range(len(nums))]
        :param nums:
        :return:
        '''
        if not nums:
            return [[]]
        res = []
        # for i in range(len(nums)):
        res.extend([nums[i]] + sub_combination
                   for i in range(len(nums))
                   for sub_combination in self.permutation(nums[:i] + nums[i + 1:])
                   )
        # for c in self.permutation(nums[:i] + nums[i+1:]):
        #     c.append(nums[i])
        #     res.append(c)
=======

class Solution:

    def permutation(self, nums):
        if not nums:
            return [[]]
        res = []
        for i in range(len(nums)):
            for c in self.permutation(nums[:i] + nums[i+1:]):
                c.append(nums[i])
                res.append(c)
>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
        return res

    def all_possible_equation2(self, nums, target):

<<<<<<< HEAD
        # operations = ['+', '-', '*', '/']

        def driver(nums):
            map = collections.defaultdict(set)
            if not nums:
                return map
            if len(nums) == 1:
                map[nums[0]].add(str(nums[0]))
=======
        operations = ['+', '-', '*', '/']

        def driver(nums):
            map = dict()
            if not nums:
                return map
            if len(nums) == 1:
                map.setdefault(nums[0], [])
                map[nums[0]].append(str(nums[0]))
>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
                return map

            # notice that end should be len(nums) - 1, otherwise, driver(nums[:i+1]) will cause infinite recursion.
            for i in range(0, len(nums) - 1):
<<<<<<< HEAD
                left = driver(nums[:i + 1])
                right = driver(nums[i + 1:])
                for key_l in left:
                    for key_r in right:
                        for op in [('+', operator.add), ('-', operator.sub),
                                   ('*', operator.mul), ('/', operator.floordiv)]:
                        # for operation in operations:
                        #     cur = None
                        #     if operation == '+':
                        #         cur = key_l + key_r
                        #     if operation == '-':
                        #         cur = key_l - key_r
                        #     if operation == '*':
                        #         cur = key_l * key_r
                        #     if operation == '/':
                        #         if key_r == 0:
                        #             continue
                        #         else:
                        #             cur = key_l // key_r
                            # handle /0 case, if key_r not 0, then cur = op[1](key_l, key_r)
                            cur = key_r and op[1](key_l, key_r)

                            for solution_l in left[key_l]:
                                for solution_r in right[key_r]:
                                    equation = solution_l + op[0] + solution_r
                                    map[cur].add("(%s)" % equation)
            return map

        res = set()
=======
                left = driver(nums[:i+1])
                right = driver(nums[i+1:])
                for key_l in left:
                    for key_r in right:
                        for operation in operations:
                            if operation == '+':
                                cur = key_l + key_r
                            if operation == '-':
                                cur = key_l - key_r
                            if operation == '*':
                                cur = key_l * key_r
                            if operation == '/':
                                if key_r == 0:
                                    continue
                                else:
                                    cur = key_l // key_r
                            map.setdefault(cur, [])
                            for solution_l in left[key_l]:
                                for solution_r in right[key_r]:
                                    equation = solution_l + operation + solution_r
                                    map[cur].append("(%s)" % equation)
            return map

        res = []
>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
        for num in self.permutation(nums):
            map = driver(num)
            # for key in map:
            #     print(key, map[key])
<<<<<<< HEAD
            res |= map[target]
=======
            res.append(map.get(target, None))

>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
        return res

    def permutations2(self, nums):
        res = []

        def driver(nums, l, r):
            if l == r:
                res.append(list(nums))
            else:
                for i in range(l, r + 1):
                    nums[l], nums[i] = nums[i], nums[l]
<<<<<<< HEAD
                    driver(nums, l + 1, r)
=======
                    driver(nums, l+1, r)
>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
                    nums[l], nums[i] = nums[i], nums[l]

        driver(nums, 0, len(nums) - 1)
        return res

<<<<<<< HEAD

res = Solution().all_possible_equation2([4, 1, 8, 7], 24)
# res = Solution().permutation([1, 2, 3])
print(res)
=======
res = Solution().all_possible_equation2([4, 1, 8, 7], 24)
# res = Solution().permutation2([1, 2, 3, 4])
print(res)
>>>>>>> d8bc092d4a25205fe45e0064a4f160d6e9bae3f5
