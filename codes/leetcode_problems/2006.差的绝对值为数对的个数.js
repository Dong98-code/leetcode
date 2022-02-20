/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var countKDifference = function(nums, k) {
    // 第一次遍历计数
    let cnt = new Map();
    let res = 0;
    for (let num of nums) {
        cnt.set(num,  (cnt[num] || 0) + 1);
    }

    for (const [key, val] of cnt) {
        res += val * (cnt[key + k] || 0);
    }
    return res;
};

nums = [1, 2, 2, 1], k = 1
console.log(countKDifference(nums, k));