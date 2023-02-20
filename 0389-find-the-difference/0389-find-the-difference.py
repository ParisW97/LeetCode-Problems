class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer = 0
        for c in s:
            answer ^= ord(c)
        for c in t:
            answer ^= ord(c)
        return chr(answer)