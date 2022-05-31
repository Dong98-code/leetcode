let n = 6;
let str = "AaAAAA".split("");

// let dp = new Array(n).fill(0).map(el => [0, 0]); // 初始化
// // 输入完为大写模式还是小写模式
// if (str[0] >= "A" && str[0] <= "Z") {
//   dp[0][0] = 2;
//   dp[0][1] = 2;
// } else {
//   dp[0][0] = 1;
//   dp[0][1] = 2;
// }

// for (let i = 1; i<n;i++) {
//   if (str[i] >= "A" && str[i] <= "Z") {
//     dp[i][0] = Math.min(dp[i-1][0]+2, dp[i-1][1]+2);
//     dp[i][1] = Math.min(dp[i-1][0]+2, dp[i-1][1]+1);
//   } else {
//     dp[i][0] = Math.min(dp[i-1][0]+1, dp[i-1][1]+2);
//     dp[i][1] = Math.min(dp[i-1][0]+2, dp[i-1][1]+2);
//   }
  
// }

// console.log(Math.min(dp[n-1][0], dp[n-1][1]));
let a = 0, b = 0;
if (str[0] >= "A" && str[0] <= "Z") {
    // dp[0][0] = 2;
    // dp[0][1] = 2;
     a = 2;
     b = 2;
    
  } else {
    // dp[0][0] = 1;
    // dp[0][1] = 2;
     a = 1;
     b = 2;
  }
  
  for (let i = 1; i<n;i++) {
    if (str[i] >= "A" && str[i] <= "Z") {
      // dp[i][0] = Math.min(dp[i-1][0]+2, dp[i-1][1]+2);
      // dp[i][1] = Math.min(dp[i-1][0]+2, dp[i-1][1]+1);
      a = Math.min(a+2, b+2);
      b = Math.min(a+2, b+1);
    } else {
      // dp[i][0] = Math.min(dp[i-1][0]+1, dp[i-1][1]+2);
      // dp[i][1] = Math.min(dp[i-1][0]+2, dp[i-1][1]+2);
      a = Math.min(a+1, b+2);
      b = Math.min(a+2, b+2);
    }
    
  }
  
  console.log(Math.min(a, b));