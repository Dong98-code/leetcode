/**
 * @param {string} n
 * @return {string}
 */
 var nearestPalindromic = function(n) {
    // n < 10
    
    if (+n < 10) {return (n-1).toString()}
    // 9999
    if ((+n + 1).toString().length === n.length + 1) {return (+n + 2).toString()}

    // 10 100 1000
    if (+(n.split("").reverse().join('')) === 1) {return (+n - 1).toString()}
    // 11 101 1001
    if ((+n - 2).toString().length === n.length - 1) {return (+n - 2).toString()}

    // 目标回文数 长度和自身相等
    // 不变 n.length
    //
    let pre = n.substr(0, n.length / 2 | 0) // n / 2 | 0向下取整： 偶数 对半， 奇数 则取到正中间的前一个
    let mid = n.length & 1? n[(n.length - 1) / 2] : ""; // & 1 : 奇数为1， 偶数为0， 奇数取中间， 偶数中间值为""

    let pre_num = pre + mid + pre.split('').reverse().join(''); 

    let ans_1, ans_2;

    if (n == pre_num){
        [ans_1, ans_2] = [change(pre, mid, "+"), change(pre, mid, "-")];
    } else if (+n < +pre_num){
        [ans_1, ans_2] = [pre_num, change(pre, mid, "-")];
    }else if (+n > +pre_num){
        [ans_1, ans_2] = [change(pre, mid, "+"), pre_num];
    }


    if (ans_1 - n < n - ans_2) return ans_1;
    return ans_2;


    function change(pre, mid, op){
        pre = pre + mid;
        if (op == "+"){
            pre = (+pre + 1).toString();
        }
        else if (op == "-"){
            pre = (pre - 1).toString();
        }
        return pre + pre.split('').reverse().join('').substr(mid.length);
    }


}

let res = nearestPalindromic('1256')