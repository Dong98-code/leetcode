# -*- coding: utf-8 -*-
# @Time : 2021/7/22 17:31
# @Author : XDD
# @File : 132.minCUt.py
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp1 = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp1[i][j] = (dp1[i + 1][j - 1] and s[i] == s[j])

        dp2 = [float("inf")] * n

        for i in range(n):
            if dp1[0][i]:
                dp2[i] = 0
            else:
                for j in range(i):
                    if dp1[j+1][i]:
                        dp2[i] = min(dp2[i], dp2[j] + 1)

        return dp2[-1]

sol = Solution()
s = "aab"
print(sol.minCut(s))
