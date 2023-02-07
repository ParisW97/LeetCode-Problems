class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[] for i in range(2**len(nums))]
        
        def flipToggle(toggle:int) -> int:
            return 0 if toggle==1 else 1
        
        for n in range(len(nums)):
            toggle = 0
            count = 2 ** n
            for i in range(len(answer)):
                if toggle == 1:
                    answer[i].append(nums[n])
                if (i+1) % count == 0:
                    toggle = flipToggle(toggle)
        
        return answer
                    