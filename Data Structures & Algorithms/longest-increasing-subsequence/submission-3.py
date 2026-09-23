class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo=[-1]*(len(nums))
    
        def dfs(i):
            if memo[i]!=-1:
                return memo[i]
            best=1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    best=max(best,dfs(j)+1)
            memo[i]=best
            return best
        return max(dfs(i) for i in range(len(nums)))