class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            subss=[]
            for subset in res:
                subss.append(subset+[num])
            res+=subss
        return res