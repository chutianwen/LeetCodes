'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

'''
from facebook.UndirectedGraphNode import UndirectedGraphNode

from collections import deque
class Solution:
	# @param node, a undirected graph node

	# We add neighbors to explored directly when iterating expanding node's frontiers
	# @return a undirected graph node
	def cloneGraph(self, node: UndirectedGraphNode):

		if not node:
			return None

		frontiers = deque()
		explored = {node.label: UndirectedGraphNode(node.label)}
		frontiers.append(node)
		while frontiers:
			expand = frontiers.popleft()
			# create a new copy node of explored node
			copy_node = explored[expand.label]

			for neighbor in expand.neighbors:
				if neighbor.label not in explored:
					new_node = UndirectedGraphNode(neighbor.label)
					explored[neighbor.label] = new_node
					frontiers.append(neighbor)
				copy_node.neighbors.append(explored[neighbor.label])

		return explored[node.label]


	def cloneGraphClassicial(self, node: UndirectedGraphNode):

		if not node:
			return None

		frontier = deque()
		frontier.append(node)
		explored = set()
		old_to_new = {node: UndirectedGraphNode(node.label)}

		while frontier:
			expand = frontier.popleft()

			explored.add(expand)
			clone_parent = old_to_new[expand]

			for kid in expand.neighbors:
				if kid not in explored and kid not in frontier:
					frontier.append(kid)
					cloned_kid = UndirectedGraphNode(kid.label)
					old_to_new[kid] = cloned_kid
				clone_parent.neighbors.append(old_to_new[kid])

		return old_to_new[node]