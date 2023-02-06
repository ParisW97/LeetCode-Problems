class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        preLen = len(strs[0])
        answer = ""

        for i in range(1,len(strs)):
            preLen = min(preLen,len(strs[i]))
        
        if preLen == 0:
            return answer
        
        for i in range(preLen):
            flag = 0
            for j in range(len(strs)):
                if j == 0:
                    temp = strs[j][i]
                elif temp != strs[j][i]:
                    temp = ""
                    flag = 1
                    break
            answer += temp
            if flag == 1:
                return answer
        return answer