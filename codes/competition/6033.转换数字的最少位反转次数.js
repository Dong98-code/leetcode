var minBitFlips = function(start, goal) {
    // 与匀速算
    res = 0;
    let tmp = (start ^ goal);
    while (tmp > 0) {
        if (tmp & 1) {
            res += 1;
        }
        tmp = tmp >> 1;
    }
    return res;
};

console.log(minBitFlips(10, 7));