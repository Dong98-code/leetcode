function f(arr, n) {
    let res = 0;
    if (n === 1) {
        return 0;
    }
    let pre = arr[0];
    let i = 1;
    while (i < n) {
        if (arr[i] > pre) {
            pre = arr[i];
            i += 1;
        } else {
            [pre,times] = f2(pre, arr[i]);
            i += 1;
            res += times;
        }
    }
    return res;
}

// function f2(pre, cur) {
//     let i = 0;
//     while (cur <= pre) {
//         i += 1;
//         cur = 2 * cur;
//     }
//     return [cur, i];
// }
function f2(pre, cur) {
    //     let i = 0;
    //     while (cur <= pre) {
    //         i += 1;
    //         cur = 2 * cur;
    //     }
    //     return [cur, i];
        let times = Math.ceil(Math.log(pre/cur)/Math.log(2))
        cur = Math.pow(2, times) * cur;
        return [cur, times]
    }

f([3, 1, 1], 3)

// console.log(Math.pow(2,3))