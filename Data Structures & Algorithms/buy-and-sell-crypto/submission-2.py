class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        for i in range(1,len(prices)):
            curr_cost=prices[i]-mini
            profit=max(profit,curr_cost)
            mini=min(mini,prices[i])
        return profit

        

        