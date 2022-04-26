let [n, p, x] = [4, 3, 2]
let arr = [2, 5, 3, 4]
let res = 0;
// let sum = 0;
let sum = arr.reduce((a, b) => a+b)
// for (let num of arr) {
//     sum += num;
// }
for (let num of arr) {
    let tmp_sum = sum - num;
    let a = tmp_sum % x;



    res += Math.floor((p + a) / x);

}