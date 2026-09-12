class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        count={}
        for num in hand:
            count[num]=count.get(num,0)+1
        hand.sort()
        for card in hand:
            if count[card]==0:
                continue 
            for i in range(card,card+groupSize):
                if count.get(i,0)==0:
                    return False 
                count[i]-=1
        return True 
