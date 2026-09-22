class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        memo=[None]*(n+1)

        def dfs(i):
            if i==len(s):
                return True 
            if memo[i] is not None:
                return memo[i]

            for word in wordDict:
                if s[i:i+len(word)]==word:
                    if dfs(i+len(word)):
                        memo[i]=True 
                        return True 
            memo[i]=False 
            return False
        return dfs(0)

                