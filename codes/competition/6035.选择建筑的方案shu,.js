/**
 * @param {string} s
 * @return {number}
 */
 var numberOfWays = function(s) {
    // 前缀和
    let n = s.length;
    let cnt_0 = new Array(n+1).fill(0);
    let cnt_1 = new Array(n+1).fill(0);

    for (let i =0; i< n; i++) {
        if (s[i] === "0") {
            cnt_0[i+1] = cnt_0[i] + 1;
            cnt_1[i+1] = cnt_1[i];
        } else {
            cnt_1[i+1] = cnt_1[i] + 1;
            cnt_0[i+1] = cnt_0[i];
        }
    }
    // 
    let res = 0;
    for (let i=0;i<n;i++) {
        if (s[i] === "0") {
            res += (cnt_1[n]-cnt_1[i+1]) * cnt_1[i];
        } else {
            res += (cnt_0[n] - cnt_0[i+1]) * cnt_0[i];
        }
    }
    return res;
};
console.log(numberOfWays("001101"));