# -*- coding: utf-8 -*-
# @Time : 2022/2/21 10:51
# @Author : XDD
# @File : 838.推多米诺.py
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 从开始 找到第一张 倒下的
        # 第一张牌默认是left
        # 最后一张默认为 right
        n = len(dominoes)
        i = 0
        left = "L"
        res = list(dominoes)
        while i < n:
            j = i
            # 第二张牌
            while j < n and dominoes[j] == ".":
                j += 1

            # 判断方向

            right = dominoes[j] if j < n else 'R'

            if right == left:
                # 相同 ，中间的牌导向这个方向
                while i < j:
                    res[i] = right
                    i += 1
            elif right == 'L' and left == 'R':
                k = j - 1
                while i < k:
                    res[i] = 'R'
                    i += 1
                    res[k] = 'L'
                    k -= 1

            left = right
            i = j + 1
        return "".join(res)


sol = Solution()
print(sol.pushDominoes(".L.R...LR..L.."))
