class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [pref[0]]
        if len(pref) == 1:
            return answer
        for i in range(len(pref)-1):
            answer.append(pref[i]^pref[i+1])
        return answer