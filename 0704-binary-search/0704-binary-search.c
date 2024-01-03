int search(int* nums, int numsSize, int target) {
    if(nums == NULL || numsSize <= 0) {
        return -1;
    }
    
    int left = 0;
    int right = numsSize - 1;
    
    while (left <= right) {
        int middle = left + (right - left) / 2;
        if(nums[middle] == target) {
            return middle;
        } else if(nums[middle] < target) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }
    return -1;
}