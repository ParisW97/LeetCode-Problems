class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pOne, pTwo = 0, 0
        mergeList = []
        
        def findMedian(nums: list) -> float:
            middle = len(nums) // 2
            if len(nums) % 2 == 1:
                return float(nums[middle])
            return (nums[middle] + nums[middle-1]) / 2
        
        def mergeRemainder(mergeList: list, nums: list, pointer: int) -> list:
            while pointer < len(nums):
                mergeList.append(nums[pointer])
                pointer += 1
            return mergeList

        if len(nums1) == 0:
            return findMedian(nums2)
        if len(nums2) == 0:
            return findMedian(nums1)
        
        while pOne < len(nums1) and pTwo < len(nums2):
            if nums1[pOne] <= nums2[pTwo]:
                mergeList.append(nums1[pOne])
                pOne += 1
            else:
                mergeList.append(nums2[pTwo])
                pTwo += 1
        if pOne < len(nums1):
            mergeList = mergeRemainder(mergeList,nums1,pOne)
        else:
            mergeList = mergeRemainder(mergeList,nums2,pTwo)

        return findMedian(mergeList)