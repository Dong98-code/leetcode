# -*- coding: utf-8 -*-
# @Time : 2021/7/19 14:10
# @Author : XDD
# @File : 91.numDecodings.py
class Solution:
    def numDecodings(self, s: str) -> int:
        # if len(s) == 0 or s[0] == "0":
        #     return 0
        # dp = [0]*(len(s)+1)
        # dp[0]=1
        # for i in range(len(s)):
        #     dp[i+1] = 0 if s[i] == "0" else dp[i]
        #     if i > 0 and (s[i-1] =="1" or (s[i-1] == "2" and s[i] <='6')):
        #         dp[i+1] = dp[i+1]+dp[i-1]
        # return dp[-1]
        if len(s) == "0" or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        cnt = 0  # 记录连续的0的个数，cnt == 2 return 0
        for i in range(len(s)):
            if s[i] == "0":
                cnt += 1
                if cnt == 2:
                    return 0
                else:
                    dp[i + 1] = 0
            else:
                cnt = 0
                dp[i + 1] = dp[i]

            if i > 0 and (s[i - 1] == "1" or (s[i - 1] == "2" and s[i] <= '6')):
                dp[i + 1] = dp[i + 1] + dp[i - 1]
        return dp[-1]

s = "100"
sol = Solution()
print(sol.numDecodings(s))
