var longestValidParentheses = function(s) {
    // 前后两次遍历
    let res = 0;
    let l = 0, r = 0;
    s = s.split("")
    for (let i=0;i < s.length;i++) {
        if (s[i] === "(") {
            l += 1;
        } else {
            r += 1;
        }
        if (l === r) {
            res = Math.max(res, 2*r);
        } else if (r > l) {
            l = 0;
            r = 0
        }
    }
    r = l = 0;
    for (let i = s.length-1;i >= 0;i--) {
        if (s[i] === "(") {
            l += 1;
        } else {
            r += 1;
        }
        if (l === r) {
            res = Math.max(res, 2*l);
        } else if (l > r) {
            l = 0;
            r = 0
        }
    }
    return res;
};
console.log(longestValidParentheses('(()'));