class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        fresh,time=0,0
        q=collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        print(q,fresh)            
        while q and fresh >0:
            for i in range(len(q)):
                row,col=q.popleft()
                print(row,col,time)
                directions=[[0,1],[1,0],[0,-1],[-1,0]]
                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if r not in range(rows) or c not in range(cols) or grid[r][c]!=1:
                        continue
                    grid[r][c] = 2
                    q.append((r,c))
                    fresh-=1
            time+=1
        return time if fresh==0 else -1
                        
                
