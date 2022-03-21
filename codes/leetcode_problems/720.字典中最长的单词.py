# -*- coding: utf-8 -*-
# @Time : 2022/3/17 23:19
# @Author : XDD
# @File : 720.字典中最长的单词.py.py
class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

    def insert(self, word):
        node = self
        for l in word:
            l = ord('l') - ord('a')
            if not node.children[l]:
                node.children[l] = Trie()
            node = node.children[l]
        node.is_end = True

    def search(self, word):
        node = self
        for l in word:
            l = ord('l') - ord('a')
            if not node.children[l]:
                return False
            node = node.children[l]
        return True


class Solution:
    def longestWord(self, words) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        num = 0
        longest = ""
        for word in words:
            if trie.search(word[:-1]) and len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                longest = word
        return longest

sol = Solution()
sol.longestWord(
["a", "banana", "app", "appl", "ap", "apply", "apple"])
