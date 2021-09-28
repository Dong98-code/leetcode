class Solution:
    def exist(self, board, word: str) -> bool:
        directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]

        m = len(board)
        n = len(board[0])
        mask = [[0] * n for _ in range(m)]

        def backtrack(i, j, board, mask, word):
            if len(word) == 0:
                return True
            # i，j为现在开始的位置， board为搜索的范围，mask用于记录是否使用过该元素，
            for direction in directions:
                cur_i = i + direction[0]
                cur_j = j + direction[1]
                if cur_i >= 0 and cur_i < m and cur_j >= 0 and cur_j < n and board[cur_i][cur_j] == word[0]:  # 只有满足边界条件才继续
                    if mask[cur_i][cur_j] == 1:
                        continue

                    mask[cur_i][cur_j] = 1
                    if backtrack(cur_i, cur_j, board, mask, word[1:]) == True:
                        return True
                    else:
                        mask[cur_i][cur_j] = 0
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # 将该元素标记为已使用
                    mask[i][j] = 1
                    if backtrack(i, j, board, mask, word[1:]) == True:
                        return True
                    else:
                        # 回溯
                        mask[i][j] = 0
        return False
# class Solution(object):
#     # 定义上下左右四个行走方向
#     directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         m = len(board)
#         if m == 0:
#             return False
#         n = len(board[0])
#         mark = [[0 for _ in range(n)] for _ in range(m)]
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     # 将该元素标记为已使用
#                     mark[i][j] = 1
#                     if self.backtrack(i, j, mark, board, word[1:]) == True:
#                         return True
#                     else:
#                         # 回溯
#                         mark[i][j] = 0
#         return False
#
#     def backtrack(self, i, j, mark, board, word):
#         if len(word) == 0:
#             return True
#
#         for direct in self.directs:
#             cur_i = i + direct[0]
#             cur_j = j + direct[1]
#
#             if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == \
#                     word[0]:
#                 # 如果是已经使用过的元素，忽略
#                 if mark[cur_i][cur_j] == 1:
#                     continue
#                 # 将该元素标记为已使用
#                 mark[cur_i][cur_j] = 1
#                 if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
#                     return True
#                 else:
#                     # 回溯
#                     mark[cur_i][cur_j] = 0
#         return False



board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
word = "aaaaaaaaaaab"
sol = Solution()
print(sol.exist(board, word))
