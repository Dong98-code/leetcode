# -*- coding: utf-8 -*-
# @Time : 2021/8/24 10:57
# @Author : XDD
# @File : 787.K站内最便宜的航线.py.py
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        # 动态规划
        dp = [[float('inf')] * (k + 2) for _ in range(n)]

        for i in range(k + 2):
            dp[src][i] = 0

        for k in range(1, k + 2):
            for flight in flights:
                # 经过k-1站到达flight[1]
                dp[flight[1]][k] = min(dp[flight[1]][k], dp[flight[0]][k - 1] + flight[2])

        res = float('inf')
        for i in range(n):
            res = min(dp[i][k + 1], res)
        return res if res != float('inf') else -1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
sol = Solution()
print(sol.findCheapestPrice(n, flights, src, dst, k))
