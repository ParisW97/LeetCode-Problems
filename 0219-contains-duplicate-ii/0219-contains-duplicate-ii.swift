class Solution {
    func containsNearbyDuplicate(_ nums: [Int], _ k: Int) -> Bool {
        var dupeMap = [Int:[Int]]()
        func validDupe(_ arr: [Int]) -> Bool{
            for left in 0...arr.count-2{
                for right in left+1...arr.count-1{
                    if abs(arr[left]-arr[right]) <= k {
                        return true
                    }
                }
            }
            return false
        }
        for (indx,val) in nums.enumerated() {
            if dupeMap.keys.contains(val) {
                dupeMap[val]?.append(indx)
                if validDupe(dupeMap[val]!) {
                    return true
                }
            } else {dupeMap[val] = [indx]}
        }
        return false
    }
}