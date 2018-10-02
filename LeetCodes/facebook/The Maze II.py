'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

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
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''

class Solution:
	def shortestDistance(self, maze, start, destination):
		"""
		:type maze: List[List[int]]
		:type start: List[int]
		:type destination: List[int]
		:rtype: int
		"""
		if not maze or len(maze) == 0:
			return False

		if not destination:
			return True

		import heapq
		from collections import defaultdict
		h, w = len(maze), len(maze[0])
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

		explored = set()

		frontier = [(0, (start[0], start[1]))]
		frontier_cost = defaultdict(int)
		frontier_cost[(start[0], start[1])] = 0

		while frontier_cost:
			cost, coordinate = heapq.heappop(frontier)

			if coordinate in frontier_cost:
				frontier_cost.pop(coordinate)
			row_p, col_p = coordinate
			if row_p == destination[0] and col_p == destination[1]:
				return cost
			explored.add((row_p, col_p))

			for direction in directions:
				row_cur, col_cur = row_p, col_p
				row_next, col_next = row_cur + direction[0], col_cur + direction[1]
				cnt = 0
				while 0 <= row_next < h and 0 <= col_next < w and maze[row_next][col_next] != 1:
					row_cur, col_cur = row_next, col_next
					row_next, col_next = row_cur + direction[0], col_cur + direction[1]
					cnt += 1

				if (row_cur, col_cur) not in explored and (row_cur, col_cur) not in frontier_cost:
					heapq.heappush(frontier, (cost + cnt, (row_cur, col_cur)))
					frontier_cost[(row_cur, col_cur)] = cost + cnt
				elif (row_cur, col_cur) in frontier_cost:
					if cost + cnt < frontier_cost[(row_cur, col_cur)] :
						heapq.heappush(frontier, (cost + cnt, (row_cur, col_cur)))
		return -1

input = [[0,0,1,0,0],
         [0,0,0,0,0],
         [0,0,0,1,0],
         [1,1,0,1,1],
         [0,0,0,0,0]]

res = Solution().shortestDistance(input, [0, 4], [4, 4])
print(res)