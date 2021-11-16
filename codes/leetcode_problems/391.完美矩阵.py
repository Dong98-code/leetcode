# -*- coding: utf-8 -*-
# @Time : 2021/11/16 22:32
# @Author : XDD
# @File : 391.完美矩阵.py
from collections import defaultdict
class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        cnt_dic = defaultdict(int)
        min_x, min_y, max_a, max_b = rectangles[0]
        arra_sum = 0
        for i in range(len(rectangles)):
            x, y, a, b = rectangles[i]
            # 计算总面积
            arra_sum += (a-x)*(b-y)
            # 寻找最小的
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)

            # 将四个顶点加入到 hash表里
            cnt_dic[(x, y)] += 1
            cnt_dic[(x, b)] += 1
            cnt_dic[(a, b)] += 1
            cnt_dic[(a, y)] += 1
        if arra_sum != (max_a-min_x)*(max_b-min_y) or cnt_dic[(min_x, min_y)] != 1 or cnt_dic[(min_x, max_b)] != 1 or cnt_dic[(max_a, min_y)] != 1 or cnt_dic[(max_a, max_b)] != 1:
            return False
        del cnt_dic[(min_x, min_y)]
        del cnt_dic[(min_x, max_b)]
        del cnt_dic[(max_a, min_y)]
        del cnt_dic[(max_a, max_b)]
        for value in cnt_dic.values():
            if value == 2 or value == 4:
                continue
            else:
                return False
        return True
sol = Solution()

rectangles = [[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]]
print(sol.isRectangleCover(rectangles))
