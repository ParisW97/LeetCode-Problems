class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magMap = {}
        for c in magazine:
            magMap[c] = magMap.get(c,0) + 1
        for c in ransomNote:
            if c not in magMap or magMap[c] == 0:
                return False
            else:
                magMap[c] -= 1
        return True