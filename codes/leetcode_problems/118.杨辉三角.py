"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""
class Solution:
    def generate(self, numRows: int):
        # ret = []
        # for row_num in range(0, numRows):
        #     rows = []
        #     for j in range(0, row_num+1):
        #         if j == 0 or j == row_num:
        #             rows.append(1)
        #         else:
        #             rows.append(ret[row_num-1][j-1]+ret[row_num-1][j])
        #     ret.append(rows[:])
        # return ret
        res = []

        for i in range(numRows):
            dp = [1] * (i + 1)
            for j in range(0, i+1):
                if j == 0 or j == i:
                    dp[j] = 1
                else:
                    dp[j] = pre[j - 1] + pre[j]
            res.append(dp[:])
            pre = dp
        return res


s = Solution()
s.generate(5)
