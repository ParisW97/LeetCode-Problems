class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numDict = {}
        for n in nums:
            numDict[n] = numDict.get(n,0) + 1
        for key in numDict.keys():
            if numDict[key] == 1:
                return key