class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[] # [t, i]
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                stackT,stackIND=stack.pop()
                res[stackIND]=i-stackIND
            stack.append((t,i))
        return res





    
            
