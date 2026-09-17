class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW,COL =len(grid), len(grid[0])
        q=deque()
        minutes=0
        
        fresh=0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1
            
    
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                directions=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]

                for dr,dc in directions:
                    if 0<=dr<ROW and 0<=dc<COL and grid[dr][dc]==1:
                        grid[dr][dc]=2
                        fresh-=1
                        q.append((dr,dc))
            minutes+=1
        if fresh==0:
            return max(0,minutes-1)
        else:
            return -1
        
                

                