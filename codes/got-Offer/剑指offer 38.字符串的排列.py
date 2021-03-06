"""
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def permutation(self, s: str):
        self.res = []
        n = len(s)

        def backtrack(s, path):
            if not s:
                self.res.append(path)
            seen = set()
            for i in range(len(s)):
                if s[i] in seen: continue
                seen.add(s[i])
                backtrack(s[:i]+s[i+1:], path + s[i])

        backtrack(s, "")
        return self.res

string = 'aab'
sol = Solution()
print(sol.permutation(string))
