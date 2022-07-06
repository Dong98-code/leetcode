var isValid = function(s) {
    let l = ['(', '{', '['];
    let r = [')', '}', ']'];
    let s_arr = s.split(""), n = s_arr.length;
    let stack = [];
    let isBalanced = true;
    let idx = 0;
    while (idx < n && isValid) {
        let item1 = s_arr[idx];
        if (l.includes(item1)) {
            stack.push(item1);
        } else {
            // 右括号
            if (stack.length === 0) {
                isBalanced = false;
            } else {
                let item2 = stack.pop();
                if (l.indexOf(item2) !== r.indexOf(item1)) {
                    isBalanced = false;
                }
            }
        }
        idx += 1;
    }
    return (isBalanced && stack.length === 0) ? true : false;

};

console.log(isValid('(]'));