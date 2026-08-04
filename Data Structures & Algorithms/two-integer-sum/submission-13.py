class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for i,name in enumerate(nums):
            diff=target-name
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[name]=i