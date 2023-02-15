class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        indx = len(num) - 1
        flag = 0
        while k > 0 or flag == 1:
            temp = k % 10
            if indx < 0:
                num.insert(0,temp+flag)
                indx = 0
            else:
                num[indx] += temp + flag
            flag = 0
            if num[indx] > 9:
                num[indx] %= 10
                flag = 1
            k = k // 10
            indx -= 1
        return num