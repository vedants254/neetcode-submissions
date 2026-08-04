class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        backetscto={'}':'{', ']':'[', ')':'('}

        for i in s:
            if i not in backetscto:
                stack.append(i)
            else:
                if stack and stack[-1]==backetscto[i]:
                    stack.pop()
                else:
                    return False 
        if not stack:
            return True 
        else:
            return False 
            

