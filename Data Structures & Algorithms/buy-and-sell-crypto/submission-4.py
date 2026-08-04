class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two pointers
        l=0
        r=1
        profit=0
        while r<(len(prices)):
            if prices[r]>prices[l]:     
                curr_cost=prices[r]-prices[l]
                profit=max(profit,curr_cost)
            else:
                l=r
            r+=1
        return profit

            

        

        