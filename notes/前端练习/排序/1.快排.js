/**
 * --- 测试用例 ---
 *
 * 输入：[1, 34, 5, 76, 8, 6, 9, 7, 6, 3]
 * 输出：[1, 3, 5, 6, 6, 7, 8, 9, 34, 76]
 *
 * --- 说明 ---
 * 
 * 思考：快速排序是稳定的吗？
 * 解答：base 的每次选择，会导致快排是不稳定排序。
 */
// 非原地
const quick_sort1 = function (nums) {
    if (nums.length < 2) {
        return nums;
    }
    let left = [];
    let right = [];
    let privot = Math.floor(nums.length / 2);
    let base = nums.splice(privot, 1)[0]; // 修改原数组，  从中删除base
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < base) {
            left.push(nums[i]);
        } else {
            right.push(nums[i]);
        }
    }
    return quick_sort1(left).concat([base], quick_sort1(right));
}

nums = [1, 34, 5, 76, 8, 6, 9, 7, 6, 3];
// console.log(quick_sort1(nums));


// 原地快排：

const quick_sort2 = function (nums, l = 0, r = nums.length - 1) {
    if (l >= r) return;
    let i = l - 1, j = r + 1, x = nums[l + r >> 1];
    while (i < j) {
        do i++; while (nums[i] < x); // 遇到第一个大于 base的值 停下来
        do j--; while (nums[j] > x);
        if (i < j) [nums[i], nums[j]] = [nums[j], nums[i]];
    }
    quick_sort2(nums, l, j);
    quick_sort2(nums, j + 1, r);
}
// const quick_sort2 = function(q, l=0, r=q.length-1)
// {
//     if (l >= r) return;

//     let i = l - 1, j = r + 1, x = q[l + r >> 1];
//     while (i < j)
//     {
//         do i ++ ; while (q[i] < x);
//         do j -- ; while (q[j] > x);
//         if (i < j) [q[i], q[j]] = [q[j], q[i]];
//     }
//     quick_sort2(q, l, j);
//     quick_sort2(q, j + 1, r);
// }

console.log(quick_sort2(nums));
console.log(nums);
