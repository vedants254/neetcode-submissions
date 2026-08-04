class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            res=0
            if tokens[i]=='+':
                o1=stack.pop()
                o2=stack.pop()
                res=((o1)+(o2))
                stack.append(res)
            elif tokens[i]=='-':
                o1=stack.pop()
                o2=stack.pop()
                res=((o2)-(o1))
                stack.append(res)
            elif tokens[i]=='*':
                o1=stack.pop()
                o2=stack.pop()
                res=((o2)*(o1))
                stack.append(res)
            elif tokens[i]=='/':
                o1=stack.pop()
                o2=stack.pop()
                res=int((float(o2)/(o1)))
                stack.append(res)
            else:
                stack.append(int(tokens[i]))

    
        return (stack[0])
    

            
            