class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited=set()
        graph={i:[] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            visited.add(node)

            for nodes in graph[node]:
                if nodes not in visited:
                    dfs(nodes)

        count=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count