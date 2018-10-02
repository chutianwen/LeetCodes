'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

from collections import defaultdict
class Solution:

	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		if not prerequisites or len(prerequisites) == 0:
			return True

		graph = defaultdict(list)
		for course, parent in prerequisites:
			graph[parent].append(course)

		dependency = defaultdict(set)

		for start in graph.keys():
			if start in dependency:
				continue

			frontier = [start]
			dependency[start] = set()
			while frontier:
				expand = frontier.pop()
				parent_dependencies = dependency[expand]

				if expand in graph:
					for child in graph[expand]:
						if child in parent_dependencies:
							return False
						if child not in dependency:
							frontier.append(child)
						dependency[child] |= parent_dependencies
						dependency[child].add(expand)

		return True


	def canFinishSet(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""

		if not prerequisites or len(prerequisites) == 0:
			return True

		dependency = defaultdict(set)
		children = defaultdict(set)

		for child, parent in prerequisites:
			for kid in children[child] | {child}:
				children[parent].add(kid)
				if parent in children[child]:
					return False

			for grand_p in dependency[parent] | {parent}:
				dependency[child].add(grand_p)
				if child == grand_p:
					return False
				for kid in children[child]:
					dependency[kid].add(grand_p)

		return True

prerequisites = [[0,1],[0,2],[1,2]]
print(Solution().canFinish(3, prerequisites))