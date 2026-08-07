class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currS=0
        maxsubarr=nums[0]
        for num in nums:
            if currS<0:
                currS=0
            currS+=num
            maxsubarr=max(maxsubarr, currS)
        return maxsubarr

        