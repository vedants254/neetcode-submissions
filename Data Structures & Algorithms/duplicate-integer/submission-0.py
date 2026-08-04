class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        if len(nums)==len(s):
            return False
        return True 
        