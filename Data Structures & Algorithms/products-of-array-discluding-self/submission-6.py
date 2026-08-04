class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            f[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            f[i]*=postfix
            postfix*=nums[i]
        return f
            
         