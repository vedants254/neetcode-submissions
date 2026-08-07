class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farmost=0
        for i in range(len(nums)):
            if i>farmost:
                return False 
            farmost= max(farmost, i+nums[i])
            if farmost>=len(nums)-1:
                return True 
        return True 
    