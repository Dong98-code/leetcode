# -*- coding: utf-8 -*-
# @Time : 2021/10/24 14:29
# @Author : XDD
# @File : 5906.句子中的有效单词.py
import  re
class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.split()
        cnt = 0
        for word in sentence:
            p = re.match(r"[a-z]+-?[a-z]+[!.,]?|[a-z]*[!.,]?", word)
            if p and p.group(0) == word:
                cnt += 1
        return cnt


sol = Solution()
sentence = "cat and  dog"
print(sol.countValidWords(sentence))


