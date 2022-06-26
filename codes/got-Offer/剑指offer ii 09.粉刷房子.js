var minCost = function(costs) {
    //DP
    let n = costs.length
    let dp = new Array(n).fill(0).map(el => new Array(3).fill(0));
    dp[0] = costs[0]
    for (let i = 1; i < n; i++) {
        dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + costs[i][0];
        dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + costs[i][1];
        dp[i][2] = Math.min(dp[i-1][1], dp[i-1][0]) + costs[i][2];
    }

    let res = Math.min(...dp[n-1]);
    return res;
};

console.log(minCost(costs = [[17,2,17],[16,16,5],[14,3,19]]));