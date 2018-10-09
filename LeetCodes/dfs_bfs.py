'''
BFS or DFS on binary tree does not need to check visited or not because each node has only one parent.
'''

def DFS_dist_from_node(query_node, parents):
    """Return dictionary containing distances of parent GO nodes from the query"""
    result = {}
    stack = []
    stack.append((query_node, 0))
    while len(stack) > 0:
        print("stack=", stack)
        node, dist = stack.pop()
        result[node] = dist
        if node in parents:
            for parent in parents[node]:
                # Get the first member of each tuple, see
                # http://stackoverflow.com/questions/12142133/how-to-get-first-element-in-a-list-of-tuples
                stack_members = [x[0] for x in stack]
                if parent not in stack_members:
                    stack.append((parent, dist + 1))
    return result


def BFS_dist_from_node(query_node, parents):
    """Return dictionary containing minimum distances of parent GO nodes from the query"""
    result = {}
    queue = []
    queue.append((query_node, 0))
    while queue:
        print("queue=", queue)
        node, dist = queue.pop(0)
        result[node] = dist
        if node in parents:  # If the node *has* parents
            for parent in parents[node]:
                # Get the first member of each tuple, see
                # http://stackoverflow.com/questions/12142133/how-to-get-first-element-in-a-list-of-tuples
                queue_members = [x[0] for x in queue]
                if parent not in result and parent not in queue_members:  # Don't visit a second time
                    queue.append((parent, dist + 1))
    return result

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_paths(graph, start, end):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))



if __name__ == "__main__":
    graph = dict()
    graph = {'N1': ['N2', 'N3', 'N4'], 'N3': ['N6', 'N7'], 'N4': ['N3'], 'N5': ['N4', 'N8'], 'N6': ['N13'],
               'N8': ['N9'], 'N9': ['N11'], 'N10': ['N7', 'N9'], 'N11': ['N14'], 'N12': ['N5']}

    print("Depth-first search:")
    dist = DFS_dist_from_node('N1', graph)
    print(dist)

    print("Breadth-first search:")
    dist = BFS_dist_from_node('N1', graph)
    print(dist)

    print("DFS recursive version 1 search:")
    res = dfs_find_target_recursive(graph=graph, node='N1', target='N9', explored=set())
    print(res)
