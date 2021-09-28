# -*- coding: utf-8 -*-
# @Time : 2021/8/7 15:11
# @Author : XDD
# @File : 392.isSubsequence.py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m + 1)]
        for i in range(1, m + 1, 1):
            for j in range(1, n + 1, 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return True if dp[m][n] == m else False


s ="abc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s,t))
