from collections import defaultdict

class Graph:
	def __init__(self, size):
		self.size = size
		self.graph = defaultdict(list)


	def addEdge(self, parent, child):
		self.graph[parent].append(child)
		self.graph[child].append(parent)

	def is_cycle(self, cur, parent, explored):

		explored.add(cur)
		for neighbor in self.graph[cur]:
			if neighbor not in explored:
				if self.is_cycle(neighbor, cur, explored):
					return True
			else:
				if neighbor != parent:
					return True

		return False

	def isTree(self):
		explored = set()

		if self.is_cycle(list(self.graph.keys())[0], -1, explored):
			return False

		return all(node in explored for node in self.graph)

graph = Graph(5)
graph.addEdge(1, 0)
graph.addEdge(0, 2)
graph.addEdge(0, 3)
graph.addEdge(3, 4)
# graph.addEdge(43, 11)
print(graph.isTree())