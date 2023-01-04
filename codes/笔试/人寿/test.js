// arr = [10, 10, 12, 12, 15, 20];
// let res = [];
// let tmp_arr = [];
// for (let num of arr) {
//   tmp_arr.push(num);
// }
// arr.sort((a, b) => a - b);
// // arr有序
// for (let num of tmp_arr) {
//   let index = arr.indexOf(num) + 1;
//   res.push(index);
// }
// console.log(res.join(","));
// function getScore(arr, nums) {
//   // m张牌的数组
//   let i = 0;
//   let res = nums[0];
//   for (let j = 0; j < arr.length; j++) {
//     i = i + arr[j];
//     res += nums[i];
//   }
//   return res;
// }
// let nums = [6, 10, 14, 2, 8, 8, 18, 5, 17];
// let arr = [1, 1, 3, 1, 2];
// console.log(getScore(arr, nums));
// let [n,m] = readline().split(" ").map(el => +el);
let [n, m] = [9, 5];
let bs = "3 1 1 0".split(" ").map((el) => +el);
let nums = "6 10 14 2 8 8 18 5 17".split(" ").map((el) => +el);
let steps = [];
for (let i = 1; i <= 4; i++) {
  let cnt = bs[i - 1];
  for (let j = 0; j < cnt; j++) {
    steps.push(i);
  }
}
// 4种牌的排列组合 然后 根据排列组合的顺序去计算 具体的分数
// 计算 score
function getScore(arr, nums) {
  // m张牌的数组
  let i = 0;
  let res = nums[0];
  for (let j = 0; j < arr.length; j++) {
    i = i + arr[j];
    res += nums[i];
  }
  return res;
}
// 计算牌的排列顺序
function permute(steps) {
  let res = [];
  const vis = new Array(steps.length).fill(false);
  const backtrack = (idx, perm) => {
    if (idx === steps.length) {
      res.push(perm.slice());
      return;
    }
    for (let i = 0; i < steps.length; i++) {
      if (vis[i] || (i > 0 && steps[i] === steps[i - 1] && !vis[i - 1])) {
        continue;
      }
      perm.push(steps[i]);
      vis[i] = true;
      backtrack(idx + 1, perm);
      vis[i] = false;
      perm.pop();
    }
  };
  backtrack(0, []);
  return res;
}
let all_steps = permute(steps);
let max_value = 0;
for (let arr of all_steps) {
  let value = getScore(arr, nums);
  max_value = Math.max(max_value, value);
}
console.log(max_value);
