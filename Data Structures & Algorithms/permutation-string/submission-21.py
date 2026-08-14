class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Hash Map: 
        count={}
        for c in s1:
            count[c]=1+count.get(c,0)
        windowlen=len(count)
        for i in range(len(s2)):
            tempw={}
            templen=0
            j=i
            while j<len(s2):
                tempw[s2[j]]=1+tempw.get(s2[j],0)
                if count.get(s2[j],0)<tempw[s2[j]]:
                    break
                if count.get(s2[j],0)==tempw[s2[j]]:
                    templen+=1
                if templen==windowlen:
                    return True 
                j+=1
        return False




