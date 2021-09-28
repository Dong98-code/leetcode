"""
输入一个英文句子，翻转句子中单词的顺序，
但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. "，则输出"student. a am I"。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # ans = ""
        # string = s.split(" ")
        # string = string[::-1]
        # # if string[-1] == " ":
        # #     string.pop()
        # # if string[0] == " ":
        # #     del string[0]
        # for item in string:
        #     if item != "":
        #         ans = ans + item+" "
        # return ans[:-1]
        s = s.strip()
        i = j = len(s) - 1
        ans = []
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            ans.append(s[i + 1: j+1])
            while s[i] == " ":
                i -= 1
            j = i
        return " ".join(ans)

sol = Solution()
s = "a good   example"
print(sol.reverseWords(s))
