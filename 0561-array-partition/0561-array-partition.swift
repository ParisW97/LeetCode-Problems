class Solution {
    func arrayPairSum(_ nums: [Int]) -> Int {
        var nums = nums.sorted()
        var answer = 0
        for i in stride(from: 0, to: nums.count - 1, by: 2) {
            answer += nums[i]
        }
        return answer
    }
}