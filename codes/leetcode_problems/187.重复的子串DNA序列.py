# -*- coding: utf-8 -*-
# @Time : 2021/10/8 13:36
# @Author : XDD
# @File : 187.重复的子串DNA序列.py
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        bin = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
        n = len(s)
        length = 10
        if n < length:
            return []
        res = []
        x = 0
        hash_dict = {}
        for i in range(n-length+1):
            if i == 0:
                for ch in s[i:i+length]:
                    x = x << 2 | bin[ch]
            else:
                # 只需要前 20位数字，
                ch = s[i+length-1]
                x = (x << 2 | bin[ch]) & ((1 << (2*length))-1)

            if x in hash_dict:
                hash_dict[x] += 1
                if hash_dict[x] == 2:
                    res.append(s[i:i+length])
            else:
                hash_dict[x] = 1
        return res

sol  = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(sol.findRepeatedDnaSequences(s))
