var minimumLines = function(stockPrices) {
    // 计算斜率
    stockPrices.sort((a, b) => a[0] - b[0]); // 按照时间升序排列
    let n = stockPrices.length;
    if (n === 1) {
        return 0;
    } else if (n === 2) {
        return 1;
    } else {
        let cnt = 1;
        let pre_dy = stockPrices[1][1] - stockPrices[0][1];
        let pre_dx = stockPrices[1][0] - stockPrices[0][0];
        for (let i = 2; i < n; i++) {
            let dy = stockPrices[i][1] - stockPrices[i-1][1];
            let dx = stockPrices[i][0] - stockPrices[i-1][0];
            if (dy * pre_dx !== dx * pre_dy) {
                cnt += 1;
            } 
            [pre_dx, pre_dy] = [dx, dy];
        }
        return cnt;
    }
    
    
};
console.log(minimumLines([[1,1],[500000000,499999999],[1000000000,999999998]]));