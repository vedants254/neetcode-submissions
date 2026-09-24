class Solution:
    def isHappy(self, n: int) -> bool:
        slow,fast=n,self.sumofsquares(n)

        while slow!=fast:
            fast=self.sumofsquares(fast)
            fast=self.sumofsquares(fast)
            slow=self.sumofsquares(slow)
        return True if fast==1 else False


    def sumofsquares(self,n):
        res=0
        while n:
            digit=n%10
            digit=digit**2
            res+=digit
            n=n//10
        return res