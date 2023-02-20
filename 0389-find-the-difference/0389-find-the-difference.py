class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charMap = {}
        for c in s:
            charMap[c] = charMap.get(c,0) + 1
        for c in t:
            if c not in charMap:
                return c
            charMap[c] -= 1
            if charMap[c] == 0:
                del charMap[c]