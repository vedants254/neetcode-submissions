class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map={')':'(',"]":'[','}':'{'}
        for i in s:
            if i in bracket_map.values():
                stack.append(i)
            elif i in bracket_map:
                if  stack and stack[-1]==bracket_map[i]:
                    stack.pop()
                else:
                    return False
        return not stack
        