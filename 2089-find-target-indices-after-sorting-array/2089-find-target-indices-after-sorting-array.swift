class Solution {
    func targetIndices(_ nums: [Int], _ target: Int) -> [Int] {
        func quickSort(_ items: inout [Int], _ fst: Int, _ lst: Int) {
            if fst >= lst {
                return
            }
            var i = fst, j = lst
            let x = items[fst + ((lst - fst) / 2)]
            while i < j {
                while items[i] < x { i += 1}
                while items[j] > x { j -= 1}
                if i <= j {
                    let tmp = items[i]
                    items[i] = items[j]
                    items[j] = tmp
                    i += 1
                    j -= 1
                }
            }
            quickSort(&items, fst, j)
            quickSort(&items, i, lst)
        }
        func sort(_ arr: [Int]) -> [Int] {
            var items = arr
            quickSort(&items, 0, items.count - 1)
            return items
        }
        var answer = [Int]()
        for (indx,val) in sort(nums).enumerated() {
            if (val == target) {
                answer.append(indx)
            }
        }
        return answer
    }
}