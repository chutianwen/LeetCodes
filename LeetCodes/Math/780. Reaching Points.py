'''
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

'''

class Solution(object):
	def reachingPoints(self, sx, sy, tx, ty):
		while tx >= sx and ty >= sy:
			if tx == ty:
				break
			elif tx > ty:
				# saving a lot while tx > ty then tx -= ty
				if ty > sy:
					tx %= ty
				else:
					return (tx - sx) % ty == 0
			else:
				if tx > sx:
					ty %= tx
				else:
					return (ty - sy) % tx == 0

		return tx == sx and ty == sy