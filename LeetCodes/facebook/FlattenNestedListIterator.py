'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].

'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
	'''
	Using a paired index to track the progress of traversing current List[NestedInteger],
	'''

	def __init__(self, nestedList):
		self.stack = [[nestedList, 0]]

	def next(self):
		if self.hasNext():
			nestedList, i = self.stack[-1]
			self.stack[-1][1] += 1
			return nestedList[i].getInteger()
		else:
			return None

	def hasNext(self):
		'''
		If current position is a pure Integer or a NestedListInteger, if latter, flatten one level of it and pushed to stack.
		:return:
		'''
		s = self.stack
		while s:
			# i, current position in this list of NestedInteger.
			nestedList, i = s[-1]
			# current list exhausted.
			if i == len(nestedList):
				s.pop()
			else:
				x = nestedList[i]
				if x.isInteger():
					return True
				s[-1][1] += 1
				s.append([x.getList(), 0])
		return False
