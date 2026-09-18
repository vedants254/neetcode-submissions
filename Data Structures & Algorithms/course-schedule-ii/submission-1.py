class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        res=[]
        visit=set()
        done=set()
        def dfs(crs):
            if crs in visit:
                return False 
            if  crs in done:
                return True  

            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            done.add(crs)
            res.append(crs)
            return True 

        for crs in range(numCourses):
            if not dfs(crs): return []

        return res 
                
