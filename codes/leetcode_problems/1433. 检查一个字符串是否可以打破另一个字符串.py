# -*- coding: utf-8 -*-
# @Time : 2022/1/7 21:09
# @Author : XDD
# @File : 1433. 检查一个字符串是否可以打破另一个字符串.py
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # 找到 s1和s2 的最小字典序排列
        # 然后比较
        s1 = list(s1)
        s1.sort()
        s2 = list(s2)
        s2.sort()
        # flag1 = True
        # flag2 = True
        #
        # for i in range(len(s1)):
        #     if ord(s1[i]) <= ord(s2[i]):
        #         continue
        #     else:
        #         flag1 = False
        #         break
        # for j in range(len(s1)):
        #     if ord(s2[j]) <= ord(s1[j]):
        #         continue
        #     else:
        #         flag2 = False
        #         break
        # return flag1 | flag2
        # check = zip(*((a >= b, a <= b) for a, b in zip(s1, s2)))
        check_1 = [(a >= b, a <= b) for a, b in zip(s1, s2)]
        check_2 = zip(*(check_1))
        # *zipped 相当与解压，返回二维矩阵的形式
        for item in check_2:
            print(item)
        return any(map(all, check_2))
s1 = "abc"
s2 = "xya"
sol = Solution()
print(sol.checkIfCanBreak(s1, s2))
