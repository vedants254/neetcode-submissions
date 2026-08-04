class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        pivot=l
         
        def binsearch(l,r):
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    return m
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return -1
        result =binsearch(0,pivot-1)
        if result!=-1:
            return result 
        return binsearch(pivot, len(nums)-1)

            
            

