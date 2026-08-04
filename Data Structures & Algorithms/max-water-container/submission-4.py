class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volm=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                base=j-i
                hnet=min(heights[j],heights[i])
                curr_volm=base*hnet
                volm=max(volm,curr_volm)
        return volm
            