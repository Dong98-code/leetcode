# -*- coding: utf-8 -*-
# @Time : 2021/8/1 22:50
# @Author : XDD
# @File : 931.minFallingPathSum.py
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == n - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + matrix[i][j]

        return min(dp[-1])

sol = Solution()
martix = [[2,1,3],[6,5,4],[7,8,9]]
print(sol.minFallingPathSum(martix))
