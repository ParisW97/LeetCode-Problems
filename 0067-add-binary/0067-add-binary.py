class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a), int(b)
        c = str(a + b)
        flag = 0
        answer = ""
        
        for i in c[::-1]:
            if int(i)+flag > 1:
                answer += str((int(i)+flag)%2)
                flag = 1
            else:
                answer += str(int(i)+flag)
                flag = 0
        if flag == 1:
            answer += "1"
        return answer[::-1]