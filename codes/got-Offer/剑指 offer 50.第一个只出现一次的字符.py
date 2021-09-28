"""在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        # f
        dic = {}
        for item in s:
            if item in dic:
                dic[item] = 0
            else:
                dic[item] = 1
        for item in s:
            if dic[item] == 1:
                return item

sol = Solution()
string = "abaccdeff"
# dic = sol.firstUniqChar(string)
print(sol.firstUniqChar(string))
