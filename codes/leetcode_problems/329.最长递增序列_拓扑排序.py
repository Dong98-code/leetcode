# -*- coding: utf-8 -*-
# @Time : 2022/1/6 13:47
# @Author : XDD
# @File : 329.最长递增序列_拓扑排序.py
import collections


class Solution:
    def longestIncreasingPath(self, matrix):
        res = 0
        m = len(matrix)
        n = len(matrix[0])
        deg_in = [0] * (m*n)  # 入度矩阵
        steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                value = matrix[i][j]
                for step in steps:
                    dx, dy = step
                    if i+dx >= 0 and i + dx < m and j+dy >= 0 and j + dy < n and matrix[i+dx][j+dy] < value:
                        deg_in[i*n+j] += 1  # 入度+1

        q = collections.deque()
        # 将入度为0的点加入到 队列中
        for i in range(m):
            for j in range(n):
                if deg_in[i*n+j] == 0:
                    q.append((i, j))  # 用元组表示 该点

        while q:
            l = len(q)
            res += 1
            for _ in range(l):
                x, y = q.popleft()  # pop出来的是一个元组
                for step in steps:
                    dx, dy = step
                    if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and matrix[x+dx][y+dy] > matrix[x][y]:
                        deg_in[(x+dx)*n+(y+dy)] -= 1
                        if deg_in[(x+dx)*n+(y+dy)] == 0:
                            q.append((x+dx, y+dy))
        return res


sol = Solution()
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(sol.longestIncreasingPath(matrix))

