var sortArrayByParity = function(nums) {
    let i = 0, j = nums.length - 1;
    
    while (i < j) {
        if ((nums[i] % 2) === 1 && (nums[j] % 2) === 0) {
        [nums[i], nums[j]] = [nums[j], nums[i]];
    }
        while (nums[i] % 2 === 0) {
            i += 1;
        }
        while (nums[j] % 2 === 1) {
            j -= 1;
        }
        
    }
    return nums;
};

arr = [3, 1, 4, 2]
console.log(sortArrayByParity(arr));