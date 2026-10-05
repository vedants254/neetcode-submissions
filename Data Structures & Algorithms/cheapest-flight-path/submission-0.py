class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for i in range(n)]
        for a,b,c in flights:
            adj[a].append([b,c])

        dist=[[float('inf')]*(k+5) for i in range(n)]
        minH=[(0,src,-1)] #(cost,node,stops)
        dist[src][0]=0

        while minH:
            cst,node,stops=heapq.heappop(minH)
            if dst==node:
                return cst
            if stops==k or dist[node][stops+1]<cst:
                continue
            for nei,w in adj[node]:
                nextcst=cst+w
                nextstops=1+stops
                if dist[nei][nextstops+1]>nextcst:
                    dist[nei][nextstops+1]=nextcst
                    heapq.heappush(minH,(nextcst,nei,nextstops))
        return -1

