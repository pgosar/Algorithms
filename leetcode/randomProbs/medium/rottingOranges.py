class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        rotten = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        mins = 0
        while rotten and fresh > 0:
            mins += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == n or yy < 0 or yy == m:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    fresh -=1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        return mins if fresh == 0 else -1
