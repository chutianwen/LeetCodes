'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down,
left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at
the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position
(excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that
the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12
Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the
border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

'''

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        dest=tuple(destination)
        m=len(maze)
        n=len(maze[0])
        res=None
        def go(start, direction):
            # return the stop position and length
            i, j = start
            ii, jj = direction
            l=0
            while 0<=i+ii<m and 0<=j+jj<n and maze[i+ii][j+jj]!=1:
                i+=ii
                j+=jj
                l+=1
            return l, (i,j)
        # bfs (dijkstra: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
        visited={}
        q=[]
        heapq.heappush(q, (0, tuple(start)))
        while q:
            length, cur = heapq.heappop(q)
            if cur in visited and visited[cur]<=length:
                continue # if cur is visited and with a shorter length, skip it.
            visited[cur]=length
            if cur == dest:
                return length
            for direction in [(-1, 0), (1, 0), (0,-1), (0,1)]:
                l, np = go(cur, direction)
                heapq.heappush(q, (length+l, np))
        return -1


'''
Approach #1 Depth First Search [Accepted]

We can view the given search space in the form of a tree. The root node of the tree represents the starting position. Four different routes are possible from each position i.e. left, right, up or down. These four options can be represented by 4 branches of each node in the given tree. Thus, the new node reached from the root traversing over the branch represents the new position occupied by the ball after choosing the corresponding direction of travel.

Maze_Tree

In order to do this traversal, one of the simplest schemes is to undergo depth first search. We make use of a recursive function dfs for this. From every current position, we try to go as deep as possible into the levels of a tree taking a particular branch traversal direction as possible. When one of the deepest levels is exhausted, we continue the process by reaching the next deepest levels of the tree. In order to travel in the various directions from the current position, we make use of a dirsdirs array. dirsdirs is an array with 4 elements, where each of the elements represents a single step of a one-dimensional movement. For travelling in a particular direction, we keep on adding the appropriate dirsdirs element in the current position till the ball hits a boundary or a wall.

We start with the given startstart position, and try to explore these directions represented by the dirsdirs array one by one. For every element dirdir of the dirsdirs chosen for the current travelling direction, we determine how far can the ball travel in this direction prior to hitting a wall or a boundary. We keep a track of the number of steps using countcount variable.

Apart from this, we also make use of a 2-D distancedistance array. distance[i][j]distance[i][j] represents the minimum number of steps required to reach the positon (i, j)(i,j) starting from the startstart position. This array is initialized with largest integer values in the beginning.

When we reach any position next to a boundary or a wall during the traversal in a particular direction, as discussed earlier, we keep a track of the number of steps taken in the last direction in countcount variable. Suppose, we reach the position (i,j)(i,j) starting from the last position (k,l)(k,l). Now, for this position, we need to determine the minimum number of steps taken to reach this position starting from the startstart position. For this, we check if the current path takes lesser steps to reach (i,j)(i,j) than any other previous path taken to reach the same position i.e. we check if distance[k][l] + countdistance[k][l]+count is lesser than distance[i][j]distance[i][j]. If not, we continue the process of traversal from the position (k,l)(k,l) in the next direction.

If distance[k][l] + countdistance[k][l]+count is lesser than distance[i][j]distance[i][j], we can reach the position (i,j)(i,j) from the current route in lesser number of steps. Thus, we need to update the value of distance[i][j]distance[i][j] as distance[k][l] + countdistance[k][l]+count. Further, now we need to try to reach the destination, destdest, from the end position (i,j)(i,j), since this could lead to a shorter path to destdest. Thus, we again call the same function dfs but with the position (i,j)(i,j) acting as the current position.

After this, we try to explore the routes possible by choosing all the other directions of travel from the current position (k,l)(k,l) as well.

At the end, the entry in distance array corresponding to the destination, destdest's coordinates gives the required minimum distance to reach the destination. If the destination can't be reached, the corresponding entry will contain Integer.MAX_VALUEInteger.MAX_VALUE.

The following animation depicts the process.

'''