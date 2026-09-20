class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={i:[] for i in range(1,n+1)}
        visited=set()
        totaltime=0
        for a,b,w in times:
            graph[a].append((b,w))

        dist={n:float('inf') for n in range(1,n+1)}

        def dfs(node,time):
            if time>=dist[node]:
                return 

            dist[node]=time
            for nei,w in graph[node]:
                dfs(nei,time+w)
        dfs(k,0)
        res=max(dist.values())
        return res if res<float('inf') else -1 
