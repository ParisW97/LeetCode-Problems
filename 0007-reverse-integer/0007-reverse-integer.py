class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        num = []
        answer = 0
        if x > -10 and x < 10:
            return x
        if x < 0:
            flag = -1
            x *= -1
        while x > 0:
            num.append(x%10)
            x = x // 10
        for n in num:
            answer *= 10
            answer += n
        answer *= flag
        if answer > (2**31)-1 or answer < -1*(2**31):
            return 0
        return answer