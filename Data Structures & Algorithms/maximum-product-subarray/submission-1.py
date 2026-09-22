class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        currmin,currmax=1,1

        for i in nums:
            if i==0:
                currmin,currmax=1,1
                continue
            tmp=currmax*i
            currmax=max(tmp,i*currmin,i)
            currmin=min(tmp,i*currmin,i)
            res=max(res,currmax)
        return res
