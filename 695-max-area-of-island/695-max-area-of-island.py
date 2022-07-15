class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def expand(x, y):
            cnt = 1
            grid[x][y] = 2
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xp, yp = x + dx, y + dy
                if 0 <= xp < m and 0 <= yp < n and grid[xp][yp] == 1:
                    cnt += expand(xp, yp)
                    
            return cnt
                    
        max_cnt = 0  
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_cnt = max(max_cnt, expand(i, j))
                        
        return max_cnt
        