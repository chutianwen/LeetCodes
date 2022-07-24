"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum
enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the
wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
Credits:
"""
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        Time: O(mn)
        Space: O(n)
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        cnt_col = [0]*n
        max_hit = 0

        cnt_row = 0
        for row in range(m):
            for col in range(n):
                if col == 0 or grid[row][col-1] == 'W':
                    cnt_row = 0
                    for cur in range(col, n):
                        if grid[row][cur] == 'W':
                            break
                        if grid[row][cur] == 'E':
                            cnt_row += 1
                if row == 0 or grid[row-1][col] == 'W':
                    cnt_col[col] = 0
                    for cur in range(row, m):
                        if grid[cur][col] == 'W':
                            break
                        if grid[cur][col] == 'E':
                            cnt_col[col] += 1
                if grid[row][col] == '0':
                    max_hit = max(max_hit, cnt_row + cnt_col[col])
        return max_hit


class Solution2(object):
    def process_left_right(self, i, grid, value):
        cnt, N, M = 0, len(grid), len(grid[0])
        for j in range(M):
            if grid[i][j] == "W":
                cnt  = 0
            elif grid[i][j] == "E":
                cnt += 1
            else:
                value[i][j] += cnt
        return

    def process_right_left(self, i, grid, value):
        cnt, N, M = 0, len(grid), len(grid[0])
        for j in range(M-1, -1, -1):
            if grid[i][j] == "W":
                cnt  = 0
            elif grid[i][j] == "E":
                cnt += 1
            else:
                value[i][j] += cnt
        return

    def process_up_down(self, j, grid, value):
        cnt, N, M = 0, len(grid), len(grid[0])
        for i in range(N):
            if grid[i][j] == "W":
                cnt  = 0
            elif grid[i][j] == "E":
                cnt += 1
            else:
                value[i][j] += cnt
        return

    def process_down_up(self, j, grid, value):
        cnt, N, M = 0, len(grid), len(grid[0])
        for i in range(N-1, -1, -1):
            if grid[i][j] == "W":
                cnt  = 0
            elif grid[i][j] == "E":
                cnt += 1
            else:
                value[i][j] += cnt
        return

    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        N, M = len(grid), len(grid[0])
        value = [[0]*M for _ in range(N)]
        self.max_bomb_enemy = 0
        for i in range(N):
            self.process_left_right(i, grid, value)
            self.process_right_left(i, grid, value)
        for j in range(M):
            self.process_up_down(j, grid, value)
            self.process_down_up(j, grid, value)
        for i in range(N):
            if value[i]:
                self.max_bomb_enemy = max(self.max_bomb_enemy, max(value[i]))
        return self.max_bomb_enemy