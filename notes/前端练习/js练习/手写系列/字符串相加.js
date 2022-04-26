const addStrings = function (num1, num2) {
    let res = [];
    let carry = 0;
    let i = num1.length - 1;
    let j = num2.length - 1;
    while (i >= 0 || j >= 0) {
        const n1 = i >= 0 ? Number(num1[i]) : 0;
        const n2 = j >= 0 ? Number(num2[j]) : 0;
        const sum = n1 + n2 + carry;
        res.unshift(sum % 10);
        carry = Math.floor(sum / 10);
        i--;
        j--;
    }
    if (carry) {
        res.unshift(carry);
    }
    return res.join("");
}