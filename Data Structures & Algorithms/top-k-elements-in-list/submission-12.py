class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for i in range(len(nums)+1)]
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
        for key,v in count.items():
            freq[v].append(key)
        arr=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                arr.append(num)
                if len(arr)==k:
                    return arr




