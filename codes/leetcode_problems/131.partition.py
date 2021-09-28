"""
131. 分割回文串
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。



示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
"""
class Solution:
    # def partition(self, s: str):
    #     n = len(s)
    #     dp = [[True] * n for _ in range(n)]
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
    #
    #     res = []
    #     path = []
    #
    #     def f(i):
    #         if i == n:
    #             res.append(path[:])
    #
    #         for j in range(i, n):
    #             if dp[i][j]:
    #                 path.append(s[i:j + 1])
    #                 f(j + 1)
    #                 path.pop()
    #
    #     f(0)
    #     return res

    def partition(self, s: str):
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])

        res = []
        path = []

        def f(i):
            if i == n:
                res.append(path[:])
            for j in range(i, n):
                if dp[i][j]:
                    path.append(s[i:j + 1])
                    f(j + 1)
                    path.pop()

        f(0)
        return res

s = "efe"
sol = Solution()
print(sol.partition(s))


