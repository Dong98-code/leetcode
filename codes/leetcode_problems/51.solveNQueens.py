"""
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。



 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。



 示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

"""
class Solution:
    def solveNQueens(self, n: int):

        # 定义一个函数 ，generate_board() 产生需要输出的格式的结果
        def generate_board():
            board = list()
            for i in range(n):
                rows[queens[i]] = "Q"
                board.append("".join(rows))
                rows[queens[i]] = '.'
            return board

        def backtrack(row: int):
            if row == n:
                board = generate_board()
                solutions.append(board)
            else:
                for i in range(n):  # i 表示的是第i列
                    if i in cols or row-i in diag1 or row+i in diag2:
                        # cols diag1 diag2 分别为三个set,用于存放不能放置皇后的位置
                        continue
                    queens[row] = i  # queues 为一个一维的list， index 维行数 row, queens[1] = 2 ,第一行的第2列放一个queen
                    cols.add(i)  # 将该列放入cols集合中
                    diag1.add(row-i)
                    diag2.add(row+i)
                    backtrack(row+1)  # 递归 求解下一行
                    cols.remove(i)
                    diag1.remove(row-i)
                    diag2.remove(row+i)

        solutions = []  # 最后返回的结果
        queens = [-1]*n
        cols = set()
        diag1 = set()
        diag2 = set()
        rows = ["."]*n
        backtrack(0)
        return solutions

sol = Solution()
print(sol.solveNQueens(4))



