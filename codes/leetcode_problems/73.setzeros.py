"""
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

进阶：

一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？
"""
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_flag = True
        col_flag = True
        # 不能在遍历的时候，遇到yige0就把他所在行所在列shewei0，这样可能会多算
        # 先遍历， 存储一个bool值，判断是否设为0
        # bool 存放在第一行，第一列
        # 单独考虑第一行第一列
        for j in range(n):
            if matrix[0][j] == 0:
                row_flag = False
                break
        for i in range(m):
            if matrix[i][0] == 0:
                col_flag = False
                break

        # 遍历，除第一行 第一列之外的值
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 遍历第一行第一列
        # for j in range(n):
        #     if matrix[0][j] == 0:
        #         for i in range(1, m):
        #             matrix[i][j] = 0
        #
        # for i in range(m):
        #     if matrix[i][0] == 0:
        #         for j in range(1, n):
        #             matrix[i][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if not col_flag:
            for i in range(m):
                matrix[i][0] = 0

        if not row_flag:
            for j in range(n):
                matrix[0][j] = 0
        return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol = Solution()
print(sol.setZeroes(matrix))
