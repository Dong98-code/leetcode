/**
 * @param {number} num
 * @return {string}
 */
var toHex = function(num) {
    if (num === 0) {
        return '0';
    }
    let res ='';
    let hex = '0123456789abcdef';
    while (num !== 0 && (res.length < 8)) {
        let index = num % 16;
        res = hex.charAt(index) + res;
        num >>= 4;
    }
    return res;
};

console.log(toHex(21))
