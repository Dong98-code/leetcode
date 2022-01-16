# -*- coding: utf-8 -*-
# @Time : 2022/1/16 13:17
# @Author : XDD
# @File : 5982.解决智力问题.py
class Solution:
    def mostPoints(self, questions) -> int:
        # 动态规划？
        n = len(questions)
        dp = [questions[-1][0]] * n  #

        for i in range(n - 2, -1, -1):
            # 倒着遍历
            if i + questions[i][1] + 1 > n - 1:
                dp[i] = max(questions[i][0], dp[i + 1])
            else:
                dp[i] = max(questions[i][0] + dp[i + questions[i][1] + 1], dp[i + 1])
        return dp[0]

sol = Solution()
print(sol.mostPoints([[3,2],[4,3],[4,4],[2,5]]))
