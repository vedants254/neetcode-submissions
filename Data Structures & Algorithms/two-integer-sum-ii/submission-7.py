class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            current=numbers[l]+numbers[r]
            if current==target:
                return [l+1,r+1]
            elif current<target:
                l=l+1
            else:
                r=r-1
        return []


        