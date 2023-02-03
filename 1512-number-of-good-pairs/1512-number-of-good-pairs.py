class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numDict = {} # number : instances
        answer = 0
        def goodPairCount(n:int):
            return 1 if (n-1) == 1 else (n-1) + goodPairCount(n-1)
            
        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1
        
        for val in numDict.values():
            if val > 1:
                answer += goodPairCount(val)
        
        return answer
