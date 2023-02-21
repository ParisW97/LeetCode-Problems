class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var sumDict = [Int:Int]() // target - num : index
        for (indx,val) in nums.enumerated() {
            if let key = sumDict[val] {
                return [key,indx]
            }
            sumDict[target-val] = indx
        }
        return []
    }
}