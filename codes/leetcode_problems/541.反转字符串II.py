# -*- coding: utf-8 -*-
# @Time : 2021/8/20 10:50
# @Author : XDD
# @File : 541.反转字符串II.py.py
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        r = n %(2*k)  # 余数
        q = n // (2*k) # 商
        res = ""

        for i in range(q):
            res += s[i*(2*k):i*(2*k)+k][::-1]+s[i*(2*k)+k:(i+1)*(2*k)]

        if r < k:
            res += s[q*(2*k):n][::-1]
        else:
            res += s[q*(2*k):q*(2*k)+k][::-1]+s[q*(2*k)+k:n]

        return res

sol = Solution()
s = "abcdefg"
k = 2
print(sol.reverseStr(s,k))
