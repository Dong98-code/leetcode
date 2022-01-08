# -*- coding: utf-8 -*-
# @Time : 2022/1/8 23:35
# @Author : XDD
# @File : 5962. 连接两字母单词得到的最长回文串.py
class Solution:
    def longestPalindrome(self, words) -> int:
        # 如果 两个字母相等 则 可以放置在任意的位置

        # 记录 相反的单词对的个数；同时 给该词对编码
        dic = {}
        num_ab = 0
        num_aa = 0  # 单独的aa
        for word in words:

            re_word = word[1] + word[0]
            if re_word != word:
                if re_word in dic and dic[re_word] > 0:
                    num_ab += 1
                    dic[re_word] -= 1  # 将这一对 -1
                elif word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1

            else:
                if word in dic and dic[word] > 0:
                    num_ab += 1
                    dic[word] -= 1
                    num_aa -= 1
                else:
                    dic[word] = 1
                    num_aa += 1
        if num_aa == 0:
            return 4 * num_ab
        else:
            return 4 * num_ab + 2

sol = Solution()
words = ["mm","mm","yb","by","bb","bm","ym","mb","yb","by","mb","mb","bb","yb","by","bb","yb","my","mb","ym"]
print(sol.longestPalindrome(words))
