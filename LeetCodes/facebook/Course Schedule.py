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


	def canFinishBetter(self, numCourses, prerequisites):
		graph = [[] for _ in range(numCourses)]
		visit = [0 for _ in range(numCourses)]
		for x, y in prerequisites:
			graph[x].append(y)

		def dfs(i):
			if visit[i] == -1:
				return False
			if visit[i] == 1:
				return True
			visit[i] = -1
			for j in graph[i]:
				if not dfs(j):
					return False
			visit[i] = 1
			return True
		for i in range(numCourses):
			if not dfs(i):
				return False
		return True


class Solution2:
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

		explored = set()
		for start in graph:
			if start in explored:
				continue
			explored.add(start)
			frontier = [(start, {start})]
			while frontier:
				expand, path = frontier.pop()
				if expand in graph:
					for kid in graph[expand]:
						if kid in path:
							return False

						if kid not in explored:
							explored.add(kid)
							path.add(kid)
							frontier.append((kid, path))
							path.remove(kid)
		return True

prerequisites = [[0,1],[0,2],[1,2]]
print(Solution().canFinish(3, prerequisites))