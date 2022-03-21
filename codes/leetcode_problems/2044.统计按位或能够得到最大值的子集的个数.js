/**
 * @param {number[]} nums
 * @return {number}
 */

 var countMaxOrSubsets = function(nums) {
    let res = new Array(1).fill(0);
    let max_num = 1;
    let ans = 0;
    for (let num of nums) {
        let tmp = [];
        for (let item of res) {
            let value = item | num;
            if (value > max_num) {
                ans  = 1;
                max_num = value;
            } else if(value === max_num) {
                ans += 1;
            }
            tmp.push(value);
        }

        res.push(...tmp);
    }
    return ans;
};

console.log(countMaxOrSubsets([3,1]));