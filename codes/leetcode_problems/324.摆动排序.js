// var wiggleSort = function(nums) {
//     let n = nums.length;
//     // 1.首先从大大小排序
//     nums.sort((a, b) => a - b);
//     let res = []
//     if (n % 2 === 0) {
//         // 偶数个， 分队
//         let k = Math.floor(n / 2);
//         for (let i = 0; i < k; i++) {
//             res.push(nums[i]);
//             res.push(nums[n-i-1])
//         }
//     } else {
//         let k = Math.floor(n/2);
//         for (let i=0; i < k; i++) {
//             res.push(nums[i]);
//             res.push(nums[n-i-1]);
//         }
//         res.push(nums[k]);
//     }
//     return res;
// };
var wiggleSort = function (nums) {
    let n = nums.length;
    // 1.首先从大大小排序
    nums.sort((a, b) => a - b);
    let res = [];
    let k = Math.floor(n / 2);
    for (let i = 0; i < k; i++) {
        res.push(nums[i]);
        res.push(nums[n - i - 1])
    }
    if (n % 2 === 1) {
        res.push(nums[k]);

    }

    return res;
};
console.log(wiggleSort([1,5,1,1,6,4]));