class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        
        if len(nums) == 2:
            return [0,1]
        
        for i in range(len(nums)):
            if nums[i] in numMap:
                return [numMap[nums[i]],i]
            numMap[target - nums[i]] = i