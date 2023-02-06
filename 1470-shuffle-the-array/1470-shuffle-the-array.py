class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y, flag = 1, n, True
        queue = []
        while y < len(nums):
            if x < n:
                queue.append(nums[x])
            if flag:
                nums[x] = nums[y]
                y += 1
                flag = False
            else:
                nums[x] = queue.pop(0)
                flag = True
            x += 1
        return nums