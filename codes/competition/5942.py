# -*- coding: utf-8 -*-
# @Time : 2021/12/5 10:42
# @Author : XDD
# @File : 5942.py
class Solution:
    def findEvenNumbers(self, digits):
        # 先排序
        # digits.sort()  # 升序排列
        ## 三重for循环
        res = set()
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        k += 1
                    else:
                        if digits[k] % 2 == 0:
                            res.add(100*digits[i]+10*digits[j]+digits[k])
        return list(res)

digits = [2,1,3,0]
sol = Solution()
print(sol.findEvenNumbers(digits))
