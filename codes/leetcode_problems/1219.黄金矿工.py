# -*- coding: utf-8 -*-
# @Time : 2022/2/5 11:17
# @Author : XDD
# @File : 1219.黄金矿工.py
import collections
class Solution:
    def getMaximumGold(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        Q = collections.deque([])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    Q.append([i, j, grid[i][j], [(i,j)]])
                    ret = max(ret, grid[i][j])
        while Q:
            i, j, total, visited = Q.popleft()
            ret = max(ret, total)
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] != 0 and (x, y) not in visited:
                    Q.append([x, y, total + grid[x][y], visited + [(x, y)]])
        return ret

sol = Solution()
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(sol.getMaximumGold(grid))
