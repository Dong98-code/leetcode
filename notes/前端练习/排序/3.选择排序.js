/**
 * --- 测试用例 ---
 *
 * 输入：[6, 45, 3, 2, 5, 6, 8, 4, 3, 4, 56, 67, 5]
 * 输出：[2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 45, 56, 67]
 *
 * --- 说明 ---
 * 
 * 思考：选择排序是稳定的吗？
 * 解答：要看代码是如何实现的，在本例中由于有交换，所以是不稳定排序。
 */

// 每次选出最小的值放在最开始的位置
const select_sort = function (nums) {
    for (let i = 0; i < nums.length-1; i++) {
        let idx = i;
        for (let j = idx + 1; j < nums.length; j++) {
            if (nums[j] < nums[idx]) {
                idx = j; // 找出最小值的索引
            }
        }
        // swap
        [nums[i], nums[idx]] = [nums[idx], nums[i]];
    }
    return nums;
}
console.log(select_sort([6, 45, 3, 2, 5, 6, 8, 4, 3, 4, 56, 67, 5]));