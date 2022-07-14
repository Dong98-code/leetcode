var firstMissingPositive = function(nums) {
    let n = nums.length;
    for (let i = 0; i< n; i++) {
        // let num = nums[i];
        while (nums[i] >= 1 && nums[i] <= n && nums[nums[i]-1] !== nums[i]) {
            const temp = nums[nums[i]-1];
            nums[nums[i]-1] = nums[i];
            nums[i] = temp;
        }
    }

    // 第二次遍历
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i+1) {
            return i+1
        }
    }
    return n+1
};
console.log(firstMissingPositive([3,4,-1,1]));