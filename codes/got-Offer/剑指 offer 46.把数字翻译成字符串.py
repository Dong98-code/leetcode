"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成
 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函
 数，用来计算一个数字有多少种不同的翻译方法。

来源：力扣（LeetCode）链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def translateNum(self, num: int) -> int:
        str_num = str(num)
        length = len(str_num)
        dp = [0]*(length+1)
        dp[0]=1
        dp[1] =1
        for i in range(2, length+1):
            tmp = str_num[i-2:i]
            dp[i] = dp[i-1] + dp[i-2] if "10" <= tmp <= "25" else dp[i-1]
        return dp[length]


sol = Solution()
print(sol.translateNum(12258))
