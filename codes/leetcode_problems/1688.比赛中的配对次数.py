# -*- coding: utf-8 -*-
# @Time : 2022/1/25 11:00
# @Author : XDD
# @File : 1688.比赛中的配对次数.py
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2 == 1:
                res += (n-1) >> 1
                n = ((n - 1) >> 1) + 1
            else:
                res += n >> 1
                n >>= 1
        return res

sol= Solution()
print(sol.numberOfMatches(7))
