"""
13. 罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        n = len(s)
        res = 0
        for i in range(n):
            if i < n-1 and (dic[s[i]] < dic[s[i+1]]):
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        return res
sol = Solution()
print(sol.romanToInt( "MCMXCIV"))
