'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].


'''


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num_dict = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        num_dict_self = {'0': '0', '1': '1', '8': '8'}

        def driver(length, isfirst):

            if length == 0:
                return ''

            if length == 1:
                return list(num_dict_self.keys())

            if length == 2:
                res = []
                for key in num_dict:
                    if isfirst and key == '0':
                        continue
                    res.append(key + num_dict[key])
                return res

            res = []
            sub_combinations = driver(length - 2, False)
            for key in num_dict:
                if isfirst and key == '0':
                    continue
                for combinations in sub_combinations:
                    res.append(key + combinations + num_dict[key])
            return res

        res = driver(n, True)

        return res


res = Solution().findStrobogrammatic(0)
print(res)
