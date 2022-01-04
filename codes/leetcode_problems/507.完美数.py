# -*- coding: utf-8 -*-
# @Time : 2022/1/3 20:21
# @Author : XDD
# @File : 507.完美数.py
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                res += i
                res += num // i

        return res == num

sol = Solution()
print(sol.checkPerfectNumber(6))
