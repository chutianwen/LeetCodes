'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
'''

class Solution:
	def addOperators(self, num, target):
		"""
		:type num: str
		:type target: int
		:rtype: List[str]
		"""
		res = []
		def calculate(num,path,last,pre):
			if not num:
				if pre==target:
					res.append(path)
				return
			n = 0
			for i in range(len(num)):
				n = 10*n + int(num[i])
				calculate(num[i+1:],path+'+'+num[:i+1],n,pre+n)
				calculate(num[i+1:],path+'-'+num[:i+1],-n,pre-n)
				calculate(num[i+1:],path+'*'+num[:i+1],n*last,pre-last+n*last)
				if i==0 and n==0:
					break
			return

		n = 0
		for i in range(len(num)):
			n = 10 * n + int(num[i])
			calculate(num[i + 1:], num[:i + 1], n, n)
			if i==0 and n==0:
				break
		return res

class Solution2:
	def addOperators(self, num, target):
		"""
		:type num: str
		:type target: int
		:rtype: List[str]
		"""
		res = []
		def calculate(num, expression, path):
			if not num:
				if sum(path)==target:
					res.append(expression)
				return
			n = 0
			for i in range(len(num)):
				n = 10*n + int(num[i])
				calculate(num[i+1:],expression+'+'+num[:i+1], path + [n])
				calculate(num[i+1:],expression+'-'+num[:i+1], path + [-n])
				tmp = path[-1]
				path[-1] *= n
				calculate(num[i+1:], expression+'*'+num[:i+1], path)
				path[-1] = tmp
				if i==0 and n==0:
					break

		n = 0
		for i in range(len(num)):
			n = 10 * n + int(num[i])
			calculate(num[i + 1:], num[:i + 1], [n])
			if i==0 and n==0:
				break
		return res

num = "105"
target = 5
res = Solution().addOperators(num, target)
print(res)


res2 = Solution2().addOperators(num, target)
print(res2)