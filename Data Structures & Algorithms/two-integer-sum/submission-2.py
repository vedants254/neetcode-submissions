class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        b=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    a=min(i,j)
                    b=max(i,j)
                    break
        return [a,b]
        