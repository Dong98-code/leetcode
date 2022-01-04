# -*- coding: utf-8 -*-
# @Time : 2022/1/4 11:13
# @Author : XDD
# @File : 2120.执行所有后缀命令.py
class Solution:
    def executeInstructions(self, n: int, startPos, s: str):
        # 500条指令，直接模拟
        m = len(s)
        ans = [0] * m
        for i in range(m):
            # 开始逐条执行， 从i处开始，起始位置 startPOS
            count_i = 0
            x, y = startPos
            for j in range(i, m):
                if s[j] == 'L':
                    x -= 1
                elif s[j] == 'R':
                    x += 1
                elif s[j] == 'U':
                    y -= 1
                else:
                    y += 1
                if x >= 0 and x < n and y >= 0 and y < n:  # 判定这次操作后 还在格子范围内
                    count_i += 1
                else:
                    # 不再格子范围内， 直接break
                    break

            ans[i] = count_i
        return ans

sol = Solution()
n = 3
startPos = [0,1]
s = "RRDDLU"
print(sol.executeInstructions(n, startPos, s))
