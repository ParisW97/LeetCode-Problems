class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = 0
        flag = False
        for c in s[::-1]:
            if flag == True and c == " ":
                return answer
            if c != " " and flag == False:
                flag = True
            if flag:
                answer += 1
        return answer