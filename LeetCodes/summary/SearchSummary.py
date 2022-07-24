'''
Summary of different search solutions. DFS + BFS + BackTracking.
Written both in recursive or iteration way.

Search has a very general methodology:

define frontier
(optionally) define explored

while frontier is not empty:
	expand = frontier.pop (can pop left or pop right)
	if expand is what we want:
		do_something() (like adding to path aggregator)

	for neighbor in nodes: (or for actions in nodes, action can bring us from current node to the neighbor)
		if neighbor is valid by meeting a criteria set (either not in explored, either not in current path, either it is reachable)
			frontier.append(neighbor) (we can append the path to it by `path + [neighbor]`

Usually we can have a cache{node: path_to_node} to record, then if the current node has a path to the next node, for path to next node, we can do:
for path in cache[node]:
	cache[next_node].append(path + [next_node])

If the action space changed for the node having same value as the one in the explored, we cannot consider them same node.
As below, head node(0) can use 1 twice and 2 once, when the right *2 reach 3, we cannot add 3 to the path 0 -> 1 -> *2, since the left *2 already
exhausted '1'. We can hash the node by (node, its action_space) as a new node to justify.

	      0
	     / \
	    1  *2
	   /    \
	   *2    3

###
For tree, since node won't point to parent node, so explored is not needed.


'''
from collections import deque, defaultdict


def dfs_find_target_recursive(graph: dict, cur: str, target: str, explored: set):
	if cur == target:
		return True

	explored.add(cur)

	for neighbor in graph[cur]:
		if neighbor not in explored:
			if dfs_find_target_recursive(graph, neighbor, target, explored):
				return True
	return False


def dfs_find_target_recursive_v2(graph: dict, cur: str, target: str, explored: set):
	if cur == target:
		return True

	for neighbor in graph[cur]:
		if neighbor not in explored:
			explored.add(neighbor)
			if dfs_find_target_recursive_v2(graph, neighbor, target, explored):
				return True
	return False


def dfs_find_target_recursive_path_v1(graph: dict, cur: str, target: str, explored: set, path: list, res: list):
	'''
	This will print one path only. Won't necessarily be the shortest path.
	'''
	if cur == target:
		res.append(path)

	explored.add(cur)
	for neighbor in graph[cur]:
		if neighbor not in explored:
			dfs_find_target_recursive_path_v1(graph, neighbor, target, explored, path + [neighbor], res)


def dfs_find_target_recursive_all_path_v1(graph: dict, cur: str, target: str, explored: set, path: list, res: list):
	'''
	In this case, we need to use back tracking to clear all the used path before iterating the next path from parent.
	'''
	if cur == target:
		res.append(path)

	explored.add(cur)
	for neighbor in graph[cur]:
		if neighbor not in explored:
			dfs_find_target_recursive_all_path_v1(graph, neighbor, target, explored, path + [neighbor], res)
	# clear this used path before returning parent node.
	explored.remove(cur)


def dfs_find_target_recursive_all_path_v2(graph: dict, cur: str, target: str, explored: set, path: list, res: list):
	'''
	In this case, we need to use back tracking to clear all the used path before iterating the next path from parent.
	'''
	if cur == target:
		res.append(path)

	for neighbor in graph[cur]:
		if neighbor not in path:
			# explored.add(cur)
			dfs_find_target_recursive_all_path_v1(graph, neighbor, target, explored, path + [neighbor], res)
			# clear this used path before returning parent node.
			# explored.remove(cur)

def bfs_find_target_iterative_all__shortest_paths(graph, cur, target):
	'''
	This can be used in word ladder II
	'''
	frontier = deque()
	frontier.append((cur, [cur]))
	explored_with_path = defaultdict(list)
	explored_with_path[cur] = [[cur]]
	result = []
	while frontier:
		expand, path = frontier.popleft()
		all_paths_to_expand = explored_with_path[expand]

		# if found the target:
		if expand == target:
			result.extend(all_paths_to_expand)

		# search in frontier
		for neighbor in graph[expand]:
			path_future = path + [neighbor]

			# if not explored, we need to add all possible shortest paths to this neighbor
			if neighbor not in explored_with_path:
				# we need to make sure node with same key is actually exactly same node, with same action space/neighbor space
				for parent_path in all_paths_to_expand:
					explored_with_path[neighbor].append(parent_path + [neighbor])
				frontier.append((neighbor, path_future))
			elif len(explored_with_path[neighbor][-1]) == len(path_future):
				explored_with_path[neighbor].append(path_future)

	return result

def bfs_find_target_iterative_all_paths(graph, cur, target):
	"""
	Comparing if the current path containing next node, this is same effect of back tracking in recursion. Make sure the same node won't appear in
	one path. However, another path can still contain this node.
	"""
	frontier = deque()
	frontier.append((cur, [cur]))
	result = []
	while frontier:
		expand, path = frontier.popleft()

		# if found the target:
		if expand == target:
			result.append(path)

		# search in frontier
		for neighbor in graph[expand]:

			# If not exist in the current path, other path can still use it though.
			if neighbor not in path:
				frontier.append((neighbor, path + [neighbor]))

	return result


if __name__ == "__main__":
	graph = dict()
	graph = {'A': ['B', 'C', 'D'],
	         'B': ['A', 'D', 'Z'],
	         'C': ['B', 'E', 'F'],
	         'D': ['A', 'E', 'F', 'Z'],
	         'E': ['H', 'I'],
	         'F': ['D', 'F', 'H', 'I', 'O'],
	         'H': [],
	         'I': ['D'],
	         'O': ["Z"],
	         "Z": []
	         }

	start, target = 'A', 'Z'
	print("\n--------------------------------------------------")
	print("DFS find target recursive version 1")
	res = dfs_find_target_recursive(graph, start, target, set())
	print(res)

	print("\n--------------------------------------------------")
	print("DFS find target recursive version 2")
	res = dfs_find_target_recursive_v2(graph, start, target, {start})
	print(res)

	print("\n--------------------------------------------------")
	print("DFS find target printing path recursive version 1")
	paths = []
	dfs_find_target_recursive_path_v1(graph, start, target, {start}, ["A"], paths)
	for path in paths:
		print(path)

	print("\n--------------------------------------------------")
	print("DFS find target printing all possible paths recursive version 1")
	paths = []
	dfs_find_target_recursive_all_path_v1(graph, start, target, set(), ["A"], paths)
	print("Total number of path from DFS:\t{}".format(len(paths)))
	for path in paths:
		print(path)

	print("\n--------------------------------------------------")
	print("DFS find target printing all possible paths recursive version 2")
	paths = []
	dfs_find_target_recursive_all_path_v2(graph, start, target, {start}, ["A"], paths)
	print("Total number of path from DFS:\t{}".format(len(paths)))
	for path in paths:
		print(path)

	print("\n--------------------------------------------------")
	print("BFS find target printing all possible shortest paths iterative version 1")
	paths = bfs_find_target_iterative_all__shortest_paths(graph, start, target)
	for path in paths:
		print(path)

	print("\n--------------------------------------------------")
	print("BFS find target printing all possible paths iterative version 1")
	paths = bfs_find_target_iterative_all_paths(graph, start, target)
	print("Total number of path from BFS:\t{}".format(len(paths)))
	for path in paths:
		print(path)
