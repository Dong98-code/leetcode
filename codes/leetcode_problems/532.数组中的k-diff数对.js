var findPairs = function(nums, k) {
    // 排序 + 双指针
    nums.sort((a, b)=> a -b);
    let res = 0;
    for (let i = 0; i < nums.length - 1;) {
        let t = nums[i] + k;
        let l = i + 1, r = nums.length-1
        while (l < r) {
            let m = l + r + 1 >> 1;
            if (nums[m] <= t) {
                l = m;
            } else {
                r = m - 1;
            }
        }
        if (nums[l] === t) {
            res += 1;
        }
        let j = i + 1;
        while (j < nums.length && nums[j] === nums[i]) {
            j++;
        }
        i = j
    }
    return res

};

console.log(findPairs([3, 1, 4, 1, 5], 2));