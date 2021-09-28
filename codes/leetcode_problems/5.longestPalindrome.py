"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[0]*n for _ in range(n)]
        # dp[i][j]=1 表示 si...sj为回文字串
        for i in range(n):
            dp[i][i] = 1

        #  递推， i <= j 才有意义
        max = 1
        begin = 1
        for j in range(1, n):
            for i in range(0, j+1):

                if s[i] != s[j]:
                    continue
                else:
                    if j - i <= 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if j-i+1 >max and dp[i][j] == 1:
                    begin = i
                    max = j-i+1

        res = s[begin:begin+max]

        return res
sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))




