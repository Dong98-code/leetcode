# -*- coding: utf-8 -*-
# @Time : 2021/8/17 10:50
# @Author : XDD
# @File : 290.单词规律.py.py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 双射
        s1 = s.split(" ")
        if len(pattern) != len(s1):
            return False

        pattern_to_str = dict()
        str_to_pattern = dict()

        for ch1, ch2 in zip(list(pattern), s1):
            if (ch1 in pattern_to_str and pattern_to_str[ch1] != ch2) or (ch2 in str_to_pattern and str_to_pattern[ch2] != ch1):
                return False
            pattern_to_str[ch1] = ch2
            str_to_pattern[ch2] = ch1

        return True

sol = Solution()

s = "dog cat cat dog"
pattern = "abba"
print(sol.wordPattern(pattern, s))
