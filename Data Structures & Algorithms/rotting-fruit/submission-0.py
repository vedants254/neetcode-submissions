class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW,COL =len(grid), len(grid[0])
        visit=set()
        q=deque()
        minutes=0
        def addcell(r,c):
            nonlocal fresh
            if (min(r,c)<0 or r==ROW or c==COL or (r,c) in visit or grid[r][c]==0):
                return 
            visit.add((r,c))
            q.append([r,c])
            fresh-=1
        
        fresh=0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c]==1:
                    fresh+=1
            
    
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)
            minutes+=1
        if fresh==0:
            return max(0,minutes-1)
        else:
            return -1
        
                

                