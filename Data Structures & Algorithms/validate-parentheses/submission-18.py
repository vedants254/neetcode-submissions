class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        backetscto={'}':'{', ']':'[', ')':'('}

        for i in s:
            if i in backetscto:
                if stack and stack[-1]==backetscto[i]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(i)
        return True if not stack else False 
            

