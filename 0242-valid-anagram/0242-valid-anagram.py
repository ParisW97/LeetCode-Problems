class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap, tMap = {}, {}
        
        for cs, ct in zip(s,t):
            sMap[cs] = sMap.get(cs,0) + 1
            tMap[ct] = tMap.get(ct,0) + 1
        
        return sMap == tMap