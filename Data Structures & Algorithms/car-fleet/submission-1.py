class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair={}
        for p,s in zip(position,speed):
            pair[p]=s
        
        stack=[]
        for p in sorted(pair, reverse=True):
            s=pair[p]
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)