from heapq import *
from collections import defaultdict

graph = defaultdict(list)
graph[1] = [2, 3, 4]
graph[2] = [6]
graph[4] = [5]
graph[5] = [3]

print(graph)

src = 1
# acc res
acc = 0
frontier = [src]
explored = defaultdict(list)
jump_limit = 5

jump_cnt = 0
while frontier and jump_cnt < jump_limit:

	expand = frontier.pop()
	if expand in explored:
		# duplicate one in frontier
		continue

	acc += expand
	jump_cnt += 1

	heapify(graph[expand])
	explored[expand] = graph[expand]

	while explored[expand]:
		child = heappop(explored[expand])
		if child not in explored:
			frontier.append(child)

print(acc)

