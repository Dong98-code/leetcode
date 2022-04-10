/**
 * @param {string} expression
 * @return {string}
 */
 var minimizeResult = function(expression) {
    // 暴力就行。可能的数据量很小
    let [l, r] = expression.split("+");
    let min = Number.MAX_VALUE;
    let res = "";
    for (let i=0;i<=l.length;i++) {
        for (let j = 0;j<=r.length;j++) {
            let tmp;
            let l_num = +(l.slice(0,i));
            l_num = l_num === 0 ? 1 : l_num;
            let r_num = +(r.slice(j, r.length));
            r_num = r_num === 0? 1 : r_num;
            let c_l = +(l.slice(i, l.length));
            let c_r= +(r.slice(0,j)); //括号中右边的数字
            if (c_l === 0 && c_r === 0) {
                tmp = l_num + r_num;
            } else if (c_l === 0) {
                tmp = l_num * c_r * r_num;
            } else if (c_r === 0) {
                tmp = r_num * c_l * l_num;
            } else {
                tmp = l_num * (c_l + c_r)*r_num;
            }
            if (tmp <= min) {
                min = tmp;
                res = l.slice(0,i) + "(" + l.slice(i, l.length) + "+" + r.slice(0,j) + ")" + r.slice(j,r.length);
            }
        }
    }
    return res;
};

console.log(minimizeResult("247+38"));