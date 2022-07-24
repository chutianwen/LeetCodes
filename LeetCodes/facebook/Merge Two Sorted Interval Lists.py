'''
/**
* 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
'''


class Solution:

	def get_intersection(self, list1:list, list2:list):

		p1 = p2 = 0
		limit_1, limit_2 = len(list1), len(list2)
		last = None
		res = []
		while p1 < limit_1 and p2 < limit_2:
			if list1[p1][0] < list2[p2][0]:
				last = self.intersect(res, last, list1[p1])
				p1 += 1
			else:
				last = self.intersect(res, last, list2[p2])
				p2 += 1

		while p1 < limit_1:
			last = self.intersect(res, last, list1[p1])
			p1 += 1

		while p2 < limit_2:
			last = self.intersect(res, last, list2[p2])
			p2 += 1

		return res

	def intersect(self, result, last, cur):
		if not last:
			return cur

		if last[1] < cur[0]:
			return cur
		else:
			if last[1] >= cur[1]:
				result.append(cur)
				return last
			else:
				result.append([cur[0], last[1]])
				return cur




t1 = [[4, 7], [9, 10], [13, 16]]
t2 = [[0, 1], [5, 9], [14, 15]]
res = Solution().get_intersection(t1, t2)
print(res)

