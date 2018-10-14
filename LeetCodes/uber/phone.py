'''
Jen coded a bot that takes a pair of integer coordinates, (x, y). She wants to move the bot to another set of coordinates. Though the bot can move any number of times, it can only make the following two types of moves:

From location (x, y) to location (x + y, y).
From location (x, y) to location (x, x + y).


For example, if the bot starts at (1, 4), it might make the following sequence of moves: (1, 4) → (5, 4) → (5, 9) → (5, 14).



You will be given starting and target ending coordinates. Determine whether the bot can reach the ending coordinates given the rules of movement.



Function Description

Complete the function canReach in the editor below. The function must return the string Yes if the bot can reach its goal, or No.



canReach has the following parameter(s):

    x1:  integer value, starting x coordinate

    y1:  integer value, starting y coordinate

    x2:  integer value, target x coordinate

    y2:  integer value, target y coordinate



Constraints

1 ≤ x1, y1, x2, y2 ≤ 1000


Input Format for Custom Testing
Sample Case 0
Sample Input 0

1
4
5
9


Sample Output 0

Yes


Explanation 0

start = (1, 4), end = (5, 9)

The bot starts at (1, 4) and makes a move of type 1, meaning that it moves to (1 + 4, 1) = (5, 4).

Then it makes a move of type 2 from (5, 4) to (5, 5 + 4) = (5, 9).

 
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'canReach' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#

# (5, 3) <- (2, 3)[+], (5, -2)[-]
# (2, 3) <- (-1, 3)[-], (2, 1)[+]

def canReachDP(x1, y1, x2, y2):
	while 1<= x2 <= 1000 and 1 <= y2 <= 1000:
		x_1, y_1 = x2 - y2, y2
		x_2, y_2 = x2, y2 - x1
		if 1<= x_1 <= 1000 and 1 <= y_1 <= 1000:
			x2, y2 = x_1, y_1
		if 1<= x_2 <= 1000 and 1 <= y_2 <= 1000:
			x2, y2 = x_2, y_2


def canReach(x1, y1, x2, y2):
	'''
	target(x2, y2)
	'''
	# Write your code here
	from collections import deque
	if x1 == x2 and y1 == y2:
		return 'Yes'

	frontier = deque()
	frontier.append((x1, y1))
	explored = set()
	explored.add((x1, y1))


	while frontier:
		x_cur, y_cur = frontier.popleft()

		for x_delta, y_delta in [(y_cur, 0), (0, x_cur)]:
			x_future, y_future = x_cur + x_delta, y_cur + y_delta
			is_boundary = 1 <= x_future <= 1000 and 1 <= y_future <= 1000
			if is_boundary:
				# reach tagest
				if x_future == x2 and y_future == y2:
					return "Yes"
				if (x_future, y_future) not in explored:
					frontier.append((x_future, y_future))
					explored.add((x_future, y_future))
	return "No"


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	x1 = int(input().strip())

	y1 = int(input().strip())

	x2 = int(input().strip())

	y2 = int(input().strip())

	result = canReach(x1, y1, x2, y2)

	fptr.write(result + '\n')

	fptr.close()
