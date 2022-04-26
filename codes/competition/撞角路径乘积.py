# -*- coding: utf-8 -*-
# @Time : 2022/4/17 11:47
# @Author : XDD
# @File : 撞角路径乘积.py
class Solution:
    def maxTrailingZeros(self, grid) -> int:
        # 以每个角为顶点 ，遍历其可能的四个方向
        def get_zero(num):
            count = 0

            while num % 10 == 0:
                count += 1
                num //= 10
            return count

        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                # 计算以grid[i][j]为起点 的上下左右四个方向的数的乘积
                l = 1
                r = 1
                u = 1
                d = 1
                if i == 0:
                    u = 0
                if i == m - 1:
                    d = 0
                if j == 0:
                    l = 0
                if j == n - 1:
                    r = 0
                for x in range(0, i + 1):
                    u = u * grid[x][j]

                for x in range(i, m):
                    d = d * grid[x][j]

                for y in range(0, j + 1):
                    l = l * grid[i][y]

                for y in range(j, n):
                    r = r * grid[i][y]

                if u != 0 and l != 0:
                    ul = u * l / grid[i][j]
                    cnt_ul = get_zero(ul)
                    res = max(res, cnt_ul)
                if u != 0 and r != 0:
                    ur = u * r / grid[i][j]
                    cnt_ur = get_zero(ur)
                    res = max(res, cnt_ur)
                if d != 0 and l != 0:
                    dl = d * l / grid[i][j]
                    cnt_dl = get_zero(dl)
                    res = max(res, cnt_dl)
                if d != 0 and r != 0:
                    dr = d * r / grid[i][j]
                    cnt_dr = get_zero(dr)
                    res = max(res, cnt_dr)
            return res

sol = Solution()
grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
print(sol.maxTrailingZeros(grid))
