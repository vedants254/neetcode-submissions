class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #nodes [1,n] range (1,n+1) | edges till n 
        # n nodes , n-1 edges

        graph={i:[] for i in range(1,len(edges)+1)}

        visited=set()

        def dfs(node,target):  #check cycle creation (default false)
            if node==target:
                return True 

            visited.add(node)

            for nei in graph[node]: #looking at nei
                if nei not in visited:
                    if dfs(nei,target):
                        return True 
            return False

        for a,b in edges:
            visited.clear()

            if dfs(a,b):
                return [a,b]

            graph[a].append(b)
            graph[b].append(a)
                    