'''
Compare different version of DFS, BFS, Shortest Path dijkstra's
To-do: BFS, dijkstra and Time complexity discussion.
Resource link:
http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
'''


class DfsFamily:

    @staticmethod
    def dfs_traversal_mark_popnode_visited(graph, start):
        '''
        If the first following vertex is B, path of this version of dfs will be ABEFC.
        Each time mark only one node as visited. Once the node pop from the stack, we should check itself visited or not.
        Like in this case, A-B-E-F-C-D-C, the last C is actually pushed at the beginning. Unlike dfs2(), this version will
        only pushed the unvisited neighbors into stack but not marking neighbor nodes as visited. Thus, we don't need to
        mark the starting point as visited, just push the start node into stack should be fine.
        *Another big difference is that, all the node pop() from stack is NOT visited, unlike dfs2(). So start node does not
        need to be marked visited initially.
        :param graph:
        :param start:
        :return:
        '''
        res = []
        visited, stack = set(), [start]
        while stack:
            # explore node
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                # res.append(vertex)
                # print("neighbors:", graph[vertex])
                # print(graph[vertex] - visited)
                stack.extend(graph[vertex] - visited)
        return visited

    @staticmethod
    def dfs_search_mark_popnode_visited(graph, start, target):
        '''
        Return only one path from start to target
        :param graph:
        :param start:
        :param target:
        :return:
        '''
        visited, candidates = set(), [(start, [start])]
        while candidates:
            cur_node, path = candidates.pop()
            if cur_node == target:
                return path
            if cur_node not in visited:
                visited.add(cur_node)
                candidates.extend([(neighbor, path + [neighbor])
                                   for neighbor in graph[cur_node] if neighbor not in visited])
        return "Target not in graph!"

    @staticmethod
    def dfs_search_all_path_mark_popnode_visited(graph, start, target):
        '''
        Return all paths from start to target. Trick part is to check if the neighbor is in current path. This is to avoid
        a loop path. Say from A-B-C-[A-B-C-A...], will become an infinite loop.
        To get all paths, we cannot use a global variable 'visited' to 'manipulate' the graph. Instead, we should use a local
        path variable for each node.
        :param graph:
        :param start:
        :param target:
        :return:
        '''
        valid_paths = []
        candidates = [(start, [start])]
        while candidates:
            cur_node, path = candidates.pop()
            if cur_node == target:
                valid_paths.append(path)
            candidates.extend([(neighbor, path + [neighbor]) for neighbor in graph[cur_node] if neighbor not in path])
        return valid_paths

    @staticmethod
    def dfs_traversal_mark_neighbor_visited(graph, start):
        '''
        If the first following vertex is B, path of this version of dfs will be ABEFD. Unlike dfs(), node 'C' won't be in
        such path because it has already been marked visited at the beginning.
        This version of dfs assumes the start point already visited. Once the node popped from the stack, there is no need
        to check such node visited or not since all nodes in stack are also known-visited. It will mark all its un-visited
        neighbor nodes as visited and pushed to the stack at the same time.
        This version of dfs may seem to have a faster speed to search target which is pretty closer to the start node.
        However it actually spends the same average time of searching, because dfs2 adds a checking step before pushing
        neighbor into stack. It may spend extra time of checking non-target neighbors.
        *Another big difference is that, all the node pop() from stack is actually already visited, unlike dfs1(). This may
        assume the start node during initial should be set as visited
        :param graph:
        :param start:
        :return:
        '''
        res = [start]
        visited, stack = {start}, [start]
        while stack:
            # start point
            vertex = stack.pop()
            # print(vertex)
            # explore unvisited neighbors
            for node in graph[vertex] - visited:
                visited.add(node)
                # res.append(node)
                stack.append(node)
        return visited

    @staticmethod
    def dfs_search_mark_neighbor_visited(graph, start, target):
        '''
        Find one path from start to target
        :param graph:
        :param start:
        :param target:
        :return:
        '''
        visited, explored = {start}, [(start, [start])]
        while explored:
            cur_node, path = explored.pop()
            for neighbor in graph[cur_node] - visited:
                if neighbor == target:
                    return path + [neighbor]
                visited.add(neighbor)
                explored.append((neighbor, path + [neighbor]))
        return "target is not in graph!"

    @staticmethod
    def dfs_search_all_path_mark_neighbor_visited(graph, start, target):
        '''
        Search all paths from start node to target
        :param graph:
        :param start:
        :param target:
        :return:
        '''
        valid_paths = []
        explored = [(start, [start])]
        while explored:
            cur_node, path = explored.pop()
            for neighbor in graph[cur_node]:
                if neighbor not in path:
                    if neighbor == target:
                        valid_paths.append(path + [neighbor])
                    explored.append((neighbor, path + [neighbor]))
        return valid_paths

    @staticmethod
    def dfs_traversal_recursive(graph, start, visited=None):
        '''
        This method is more like dfs_traversal_mark_popnode_visited()
        :param graph:
        :param start:
        :param visited:
        :return:
        '''
        if visited is None:
            visited = set()
        # This is not necessary in the algorithm, but in logic it makes sense. Unnecessary is because of using set().
        # This will help quick return, specially for circle case.
        # if start in visited:
        #     return
        # print(start)
        visited.add(start)
        # print(graph[start] - visited)
        for neighbor in graph[start] - visited:
            DfsFamily.dfs_traversal_recursive(graph, neighbor, visited)
        return visited

    @staticmethod
    def dfs_search_recursive(graph, start, target, visited=None, cur_path=None):
        '''
        Has to determine returned valid_path is None or real valid. Think case like A-B-D, if return D directly, then the
        final result will return None.
        :param graph:
        :param start:
        :param target:
        :param visited:
        :param cur_path:
        :return:
        '''
        if not visited:
            visited = set()
        if not cur_path:
            cur_path = [start]
        if start == target:
            return cur_path
        visited.add(start)
        for neighbor in graph[start] - visited:
            valid_path = DfsFamily.dfs_search_recursive(graph, neighbor, target, visited, cur_path + [neighbor])
            if valid_path:
                return valid_path
        return None

    @staticmethod
    def dfs_search_all_path_recursive(graph, start, target, cur_path=None):
        '''
        Fancy way of using yield.
        :param graph:
        :param start:
        :param target:
        :param cur_path:
        :return:
        '''
        if cur_path is None:
            cur_path = [start]
        if start == target:
            yield cur_path
        for neighbor in graph[start] - set(cur_path):
            # yield from a generator
            yield from DfsFamily.dfs_search_all_path_recursive(graph, neighbor, target, cur_path + [neighbor])

    @staticmethod
    def dfs_search_all_path_recursive2(graph, start, target, cur_path=None):
        '''
        return [cur_path] rather than 'cur_path' is very important, since we are using extend()
        :param graph:
        :param start:
        :param target:
        :param cur_path:
        :return:
        '''
        if cur_path is None:
            cur_path = [start]
        if start == target:
            return [cur_path]
        valid_paths = []
        for neighbor in graph[start] - set(cur_path):
            # yield from a generator
            sub_paths = DfsFamily.dfs_search_all_path_recursive2(graph, neighbor, target, cur_path + [neighbor])
            valid_paths.extend(sub_paths)
        return valid_paths

if __name__ == "__main__":

    graph = {'A': {'B', 'C'},
             'B': {'D', 'E'},
             'C': {'F'},
             'D': {'B'},
             'E': {'B', 'F'},
             'F': {'C', 'E'}}

    print("{}{}{}".format("-" * 15, "Two versions of iterative methods of DFS", "-" * 15))

    # {'E', 'D', 'F', 'A', 'C', 'B'}
    dfs_traversal = DfsFamily.dfs_traversal_mark_popnode_visited(graph, 'A')
    print("{:50s}:{}".format("dfs_traversal_mark_popnode_visited", dfs_traversal))

    path = DfsFamily.dfs_search_mark_popnode_visited(graph, 'A', 'C')
    print("{:50s}:{}".format("dfs_search_mark_popnode_visited", path))

    path = DfsFamily.dfs_search_all_path_mark_popnode_visited(graph, 'A', 'C')
    print("{:50s}:{}".format("dfs_search_all_path_mark_popnode_visited", path))

    print("-" * 50)

    dfs_traversal = DfsFamily.dfs_traversal_mark_neighbor_visited(graph, 'A')
    print("{:50s}:{}".format("dfs_traversal_mark_neighbor_visited", dfs_traversal))

    path = DfsFamily.dfs_search_mark_neighbor_visited(graph, 'A', 'C')
    print("{:50s}:{}".format("dfs_search_mark_neighbor_visited", path))

    path = DfsFamily.dfs_search_all_path_mark_neighbor_visited(graph, 'A', 'C')
    print("{:50s}:{}".format("dfs_search_all_path_mark_neighbor_visited", path))

    print("{}{}{}".format("-" * 15, "Recursive version of DFS", "-" * 15))

    dfs_traversal = DfsFamily.dfs_traversal_recursive(graph, 'A')
    print("{:50s}:{}".format("dfs_traversal_recursive", dfs_traversal))

    path = DfsFamily.dfs_search_recursive(graph, 'A', 'C')
    print("{:50s}:{}".format("dfs_search_recursive", path))

    path = list(DfsFamily.dfs_search_all_path_recursive(graph, 'A', 'C'))
    print("{:50s}:{}".format("dfs_search_all_path_recursive", path))

    path = DfsFamily.dfs_search_all_path_recursive2(graph, 'A', 'C')
    print("{:50s}:{}".format("dfs_search_all_path_recursive2", path))




