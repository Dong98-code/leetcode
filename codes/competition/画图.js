n = 4;
for (let i = 0; i < 2 * n - 1; i++) {
    let res = new Array(2 * n - 1).fill(" ");
    if (i < n - 1) {
        if (i === 0) {
            res[0] = "*";
            for (let j = n - 1; j < 2 * n - 1; j++) {
                res[j] = "*";
            }
        } else {
            res[0] = "*";
            res[n - 1] = "*";
            res[i] = "*";
            res[2 * n - 1 - i] = "*"
        }
    } else if (i === n - 1) {
        res = new Array(2 * n - 1).fill("*");
    } else if (i >= n) {
        if (i === 2 * n - 2) {
            // 最后一行
            res[2 * n - 2] = "*";
            for (let j = 0; j < n; j++) {
                res[j] = "*";
            }
        }
         else {
                let m = (i + 1) % n;
                res[n - 1] = "*";
                res[2 * n - 1] = "*";
                res[n - 1 - m] = "*";
                res[n - 1 + m] = "*";
            }

        }
        console.log();(res.join(""));
}