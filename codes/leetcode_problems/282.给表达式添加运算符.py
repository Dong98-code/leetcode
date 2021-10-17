# -*- coding: utf-8 -*-
# @Time : 2021/10/16 20:13
# @Author : XDD
# @File : 282.给表达式添加运算符.py
class Solution:
    def addOperators(self, num: str, target: int):
        n = len(num)
        ans = []
        def dfs(expr:list, i:int, res, prev):
            """

            :param expr: 用list填装表达式的值
            :param i: 当前的位置
            :param res: 当前的计算结果的位置
            :param prev: 上一个连续乘积 的值
            :return:
            """
            if i == n:
                if res == target:
                    ans.append("".join(expr))
                return
            sign_index = len(expr)  # 符号位的位置
            if i > 0:
                expr.append(' ')  # 符号位占位
            val = 0
            for j in range(i, n):
                if j > i and num[i] == "0":
                    break
                val = val*10 + int(num[j])  # 当前运算位 的数值
                expr.append(num[j])
                if i == 0:
                    dfs(expr, j+1, val, val)
                else:
                    expr[sign_index] = "+"; dfs(expr, j+1, res+val, val)
                    expr[sign_index] = "-"; dfs(expr, j+1, res-val, val)
                    expr[sign_index] = "x"; dfs(expr, j+1, res-prev+prev*val, prev*val)
            del expr[sign_index:]

        dfs([], 0, 0, 0)
        return ans

sol = Solution()
num = "123"
target = 6
sol.addOperators(num, target)
