class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        curr=0
        for i in range(len(nums)):
            if curr<0:
                curr=0
            curr+=nums[i]
            maxsum=max(maxsum,curr)

        return maxsum