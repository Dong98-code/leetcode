# -*- coding: utf-8 -*-
# @Time : 2021/11/4 10:19
# @Author : XDD
# @File : 367.有效的完全平方数.py
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while num > 0:
            num -= 2 * i + 1
            i += 1
        return num == 0
