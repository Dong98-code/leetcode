# -*- coding: utf-8 -*-
# @Time : 2021/9/16 10:31
# @Author : XDD
# @File : 212.单词搜索

# # 首先实现前缀树
# class Trie:
#     def __init__(self):
#         """
#         初始化
#         """
#         self.children = [None] * 26
#         self.is_end = False
#         self.word = ''
#
#     def insert(self, word: str):
#         """
#         插入一个单词到树中
#         """
#         node = self
#         for letter in word:
#             letter = ord(letter) - ord('a')
#             if not node.children[letter]:
#                 node.children[letter] = Trie()  # 初始化一个树节点
#             node = node.children[letter]  # 更新当前结点的位置
#         node.word = word
#
#
# class Solution:
#     def findWords(self, board, words):
#
#         # 将words中的单词插入到Trie中
#
#         trie = Trie()
#         for word in words:
#             trie.insert(word)
#
#         def dfs(now, i1, j1):
#             # 递归结束条件
#             ch = board[i1][j1]
#
#             letter = ord(ch) - ord('a')
#             if letter not in range(26) or not now.children[letter]:
#                 return
#
#             now = now.children[letter]
#             if now.word !='':
#                 ans.add(now.word)
#
#             board[i1][j1] = "#"
#             for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
#                 if i2 >= 0 and i2 < m and j2 >= 0 and j2 < n:
#                     dfs(now, i2, j2)
#             board[i1][j1] = ch
#
#         ans = set()
#         m, n = len(board), len(board[0])
#         for i in range(m):
#             for j in range(n):
#                 dfs(trie, i, j)
#         return list(ans)
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            now = now.children[ch]
            if now.word != "":
                ans.add(now.word)

            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch

        ans = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(ans)


sol = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(sol.findWords(board, words))

