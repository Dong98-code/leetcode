/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
var missingRolls = function(rolls, mean, n) {
    let sum = 0;
    for (let i=0;i<rolls.length;i++) {
        sum += rolls[i];
    }
    let m = rolls.length;
    let target = mean*(n+m) - sum;
    if ((target > n*6) || (target < n)) {
        return [];
    }
    let res = [];
    let base = Math.floor(target/n);
    let remain = target % n;
    for (let i=0;i<remain;i++)  {
        res.push(base+1);
    }
    for (let i=remain;i<n;i++) {
        res.push(base);
    }
    return res;

};
console.log(missingRolls(rolls=[3,2,4,3], mean=4, n=2));