
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic={}

        for i in s:
            dic[i]=dic.get(i,0)+1
        
        for j in t:
            if j in dic.keys() and dic[j]>0:
                dic[j]-=1
                if dic[j]==0:
                    del dic[j]
                continue
            
            if j not in dic.keys()  :
                return j
            
        