class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = self.findFreq(s)
        dictT = self.findFreq(t)
        if len(dictS.keys()) != len(dictT.keys()):
            return False
        for x in dictS:
            if not x in dictT.keys() or dictS[x] != dictT[x]:
                return False
        return True
    
    def findFreq(self, s: str) -> dict:
        dict = {}
        for x in s:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        return dict
    
        
    