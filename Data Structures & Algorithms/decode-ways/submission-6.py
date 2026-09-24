class Solution:
    def numDecodings(self, s: str) -> int:
        memo=[-1]*(len(s))

        def dfs(i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            if memo[i]!=-1:
                return memo[i]
            count=dfs(i+1)

            if i+1<len(s) and int(s[i:i+2])<=26:
                count+=dfs(i+2)
            memo[i]=count
            return count
        return dfs(0)