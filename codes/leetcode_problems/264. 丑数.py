# -*- coding: utf-8 -*-
# @Time : 2022/3/10 18:07
# @Author : XDD
# @File : 264. 丑数.py
class Solution:

    def nthUglyNumber(self, n: int) -> int:
        def dp(res, i, a, b, c, n):
            if (i == n):
                return
            n2 = res[a]*2
            n3 = res[b]*3
            n5 = res[c]*5
            res[i] = min(n2, n3, n5)
            if n2 <= res[i]:
                a += 1
            if n3 <= res[i]:
                b += 1
            if n5 <= res[i]:
                c += 1
            dp(res, i+1, a, b, c, n)

        res = [0]*n
        a = 0
        b = 0
        c = 0
        res[0] = 1
        i = 1
        dp(res, i, a, b, c, n)
        return res[n-1]

sol = Solution()
print(sol.nthUglyNumber(10))
