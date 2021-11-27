# -*- coding: utf-8 -*-
# @Time : 2021/11/27 10:51
# @Author : XDD
# @File : 519.随机反转矩阵.py
import random


class Solution:

    def __init__(self, m: int, n: int):
        # matrix = [[0 for _ in range(n)] for _ in range(m)]
        # self.matrix = matrix
        # self.ori = matrix.copy()
        # self.total = m * n  # 总数
        # index = [i for i in range(m*n)]
        # self.index_ori = index.copy()
        # self.index = index
        self.m = m
        self.n = n
        self.map = {}
        self.total = m * n

    def flip(self):
        x = random.randint(0, self.total - 1)
        # 获取下标
        # r = self.index[j] // self.n
        # c = self.index[j] % self.n
        # self.index[j], self.index[self.total-1] = self.index[self.total-1], self.index[j]

        # self.matrix[r][c] = 1
        self.total -= 1
        # return [r, c]
        idx = self.map.get(x, x)
        # 将位置 x 对应的映射设置为位置 total 对应的映射
        self.map[x] = self.map.get(self.total, self.total)  # 键不存在，返回默认值
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        # self.matrix = self.ori.copy()
        # self.index = self.index_ori.copy()
        self.total = self.m * self.n
        self.map.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

# Your Solution object will be instantiated and called as such:
obj = Solution(3, 1)
param_1 = obj.flip()
param_2 = obj.flip()
param_3 = obj.flip()


obj.reset()

