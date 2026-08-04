class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxsum=0
        while l<r:
            currsum=min(heights[l],heights[r])*(r-l)
            maxsum=max(maxsum,currsum)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxsum

                 
                


            
                
                

            