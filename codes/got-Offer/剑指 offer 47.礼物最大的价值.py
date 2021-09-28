"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def maxValue(self, grid):
        # dp
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[0]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i >= 1 and j >= 0:
        #             dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        #         elif i >= 1 and j == 0:
        #             dp[i][j] = dp[i-1][j]+grid[i][j]
        #         elif i == 0 and j >= 1:
        #             dp[i][j] = dp[i][j-1]+grid[i][j]
        #         else:
        #             dp[i][j] = grid[0][0]
        # return dp[m-1][n-1]
        m = len(grid)
        n = len(grid[0])
        # dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # if i >= 1 and j >= 1:
                #     dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i][j]
                # elif i >= 1 and j == 0:
                #     dp[i][j] = dp[i-1][j]+grid[i][j]
                # elif i==0 and j>=1:
                #     dp[i][j] = dp[i][j-1]+grid[i][j]
                # else:
                #     dp[i][j] = grid[0][0]
                if i == 0 and j == 0:
                    grid[i][j] = grid[i][j]
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[m - 1][n - 1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
sol = Solution()
print(sol.maxValue(grid))
