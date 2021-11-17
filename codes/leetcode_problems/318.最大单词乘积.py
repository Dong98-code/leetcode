# -*- coding: utf-8 -*-
# @Time : 2021/11/17 11:09
# @Author : XDD
# @File : 318.最大单词乘积.py
class Solution:
    def maxProduct(self, words) -> int:
        def has_same(word1, word2):
            set_1 = set(list(word1))
            set_2 = set(list(word2))
            b = set_1.isdisjoint(set_2)
            return b

        n = len(words)
        max_num = 0
        for i in range(n):
            for j in range(i + 1, n):
                if has_same(words[i], words[j]):
                    max_num = max(max_num, len(words[i]) * len(words[j]))

        return max_num

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
sol = Solution()
print(sol.maxProduct(words))
