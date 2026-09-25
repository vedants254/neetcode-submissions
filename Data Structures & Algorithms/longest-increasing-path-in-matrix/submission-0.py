class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        ROW,COL=len(matrix), len(matrix[0])
        dp={}
        def dfs(i,j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=1
            for r,c in directions:
                if (0<=i+r<ROW and 0<=j+c<COL and matrix[i+r][j+c]>matrix[i][j]):
                    dp[(i,j)]=max(dp[(i,j)],1+dfs(i+r,j+c))
        
            return dp[(i,j)]
        return max(dfs(i, j) for i in range(ROW) for j in range(COL))