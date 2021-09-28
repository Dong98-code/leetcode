class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False

        dp = [[True] * l1 for _ in range(l2)]
        for i in range(1, l2):
            dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1])
        for j in range(1, l1):
            dp[0][j] = dp[0][j - 1] and (s2[j - 1] == s3[j - 1])

        for i in range(1, l2):
            for j in range(1, l1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                            dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[l2 - 1][l1 - 1]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aabccdbbca"
sol = Solution()
print(sol.isInterleave(s1,s2,s3))
