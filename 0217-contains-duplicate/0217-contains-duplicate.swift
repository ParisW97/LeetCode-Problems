class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var foo = Set<Int>()
        for num in nums {
            let bar = foo.count
            foo.insert(num)
            if foo.count == bar {return true}
        }
        return false
    }
}