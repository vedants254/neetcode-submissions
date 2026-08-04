class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zcount=0
        for num in nums:
            if num:
                prod*=num
            else:
                zcount+=1
        if zcount>1: return [0]*len(nums)

        res=[0]*len(nums)
        for i,c in enumerate(nums):
            if zcount>1:
                return res
            elif zcount==1:
                if c==0:
                    res[i]=prod
                else:
                    res[i]=0
            else:
                res[i]=prod//c
        return res

