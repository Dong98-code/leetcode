"""
6. Z 字形变换
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dp = [[] for _ in range(numRows)]
        # 每一个循环里面有 2n-2个字符，取余数
        for i in range(len(s)):
            k = i%(2*numRows-2)
            if k <= numRows -1:
                dp[k].append(s[i])
            else:
                dp[2*numRows-2-k].append(s[i])
        res = ""
        for i in range(numRows):
            for item in dp[i]:
                res += item
        return res
sol = Solution()
s = "PAYPALISHIRING"
print(sol.convert(s, 4))
