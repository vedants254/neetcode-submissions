class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenset=set()
        for n in nums:
            if n in seenset:
                return True 
            seenset.add(n) 
        return False 


        