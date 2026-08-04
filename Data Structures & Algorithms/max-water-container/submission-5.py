class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volm=0
        l=0
        r=len(heights)-1
        while l<r:
            base=r-l
            hnet=min(heights[l],heights[r])
            curr_volm=base*hnet
            volm=max(volm,curr_volm)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return volm


            