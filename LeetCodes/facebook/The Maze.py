'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

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

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''

class Solution:
	def hasPath(self, maze, start, destination):
		"""
		If size of maze is N*N, then Time is O(N * N) * O(N), O(#state)*O(f(state)), in this case, f(state) seems to be O(N), but it averagely
		belongs to O(1)
		
		:type maze: List[List[int]]
		:type start: List[int]
		:type destination: List[int]
		:rtype: bool
		"""
		if not maze or len(maze) == 0:
			return False

		if not destination:
			return True

		from collections import deque
		h, w = len(maze), len(maze[0])
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

		explored = set()
		explored.add((start[0], start[1]))
		frontier = deque()
		frontier.append((start[0], start[1]))
		while frontier:
			row_p, col_p = frontier.popleft()

			for direction in directions:
				row_cur, col_cur = row_p, col_p
				row_next, col_next = row_cur + direction[0], col_cur + direction[1]
				while 0 <= row_next < h and 0 <= col_next < w and maze[row_next][col_next] != 1:
					row_cur, col_cur = row_next, col_next
					row_next, col_next = row_cur + direction[0], col_cur + direction[1]

				if row_cur == destination[0] and col_cur == destination[1]:
					return True

				if (row_cur, col_cur) not in explored:
					explored.add((row_cur, col_cur))
					frontier.append((row_cur, col_cur))

		return False

input = [[0,0,1,0,0],
         [0,0,0,0,0],
         [0,0,0,1,0],
         [1,1,0,1,1],
         [0,0,0,0,0]]

res = Solution().hasPath(input, [0, 4], [4, 4])
print(res)