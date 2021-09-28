class Solution:
    def minPathSum(self, grid) -> int:
        # 动态规划
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1]+grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid
sol = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(sol.minPathSum(grid))
