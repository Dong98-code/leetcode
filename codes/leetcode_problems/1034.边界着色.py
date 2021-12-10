# -*- coding: utf-8 -*-
# @Time : 2021/12/7 14:09
# @Author : XDD
# @File : 1034.边界着色.py
class Solution:
    def colorBorder(self, grid, row: int, col: int, color: int):
        # 第一步 寻找联通区域
        m = len(grid)
        n = len(grid[0])
        mask = [[0 for _ in range(n)] for _ in range(m)]
        # mask[row][col] = 1

        # dfs 寻找联通区域
        def dfs(grid, x, y, pre, mask):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != pre or mask[x][y] == 1:
                return
            mask[x][y] = 1
            dfs(grid, x - 1, y, pre, mask)
            dfs(grid, x, y - 1, pre, mask)
            dfs(grid, x + 1, y, pre, mask)
            dfs(grid, x, y + 1, pre, mask)

        pre = grid[row][col]  # 开始位置的颜色
        dfs(grid, row, col, pre, mask)  # 得到联通区域mask
        for i in range(m):
            for j in range(n):
                if mask[i][j] == 1:  # 判断是都是联通区域
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        grid[i][j] = color
                    elif mask[i - 1][j] != 1 or mask[i][j - 1] != 1 or mask[i + 1][j] != 1 or mask[i][j + 1] != 1:
                        grid[i][j] = color
                    else:
                        continue
        return grid

sol = Solution()
grid = [[1,1,1],[1,1,1],[1,1,1]]
row = 1
col = 1
color = 2
print(sol.colorBorder(grid, row, col, color))
