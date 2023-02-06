class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numList = []
        while x > 0:
            numList.append(x%10)
            x = x // 10
        numList = numList[::-1]
        left, right = 0, len(numList)-1
        while left < right:
            if numList[left] != numList[right]:
                return False
            left += 1
            right -= 1
        return True