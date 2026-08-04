class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
       
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i!=j:
                    product=product*nums[j]
                else:
                    continue
            l.append(product)
        return l
            