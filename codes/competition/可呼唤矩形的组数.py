# -*- coding: utf-8 -*-
# @Time : 2021/9/12 11:03
# @Author : XDD
# @File : 可呼唤矩形的组数.py
from functools import reduce


class Solution:
    def interchangeableRectangles(self, rectangles) -> int:
        # 哈希，依次遍历计算长宽比
        dic = {}  # key:为长宽比，value为个数，通过计算排列组合数得到最终的结果
        n = len(rectangles)
        for i in range(n):
            ratio = rectangles[i][0] / rectangles[i][1]
            if ratio in dic:
                dic[ratio] += 1
            else:
                dic[ratio] = 1

        ans = 0

        # 遍历字典， values = 1， 则 没有可以配对的 Cm2
        for _, value in dic.items():
            if value == 1:
                ans += 0
            else:
                ans += reduce(lambda x, y: x * y, range(1, value + 1)) / (
                            2 * reduce(lambda x, y: x * y, range(1, value - 1)))
        return ans
sol = Solution()
print(sol.interchangeableRectangles([[1,7],[2,8],[8,8],[2,5],[2,8],[7,4]]))
