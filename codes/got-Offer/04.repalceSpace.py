"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""
import re

class Solution:
    def replaceSpace(self, s: str) -> str:
        # ret = re.compile(" ")
        # return ret.sub("%20", s)
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == " ":
                s_list[i] = "%20"
        return "".join(s_list)
if __name__ == "__main__":
    solu = Solution()
    s = "We are happy."
    print(solu.replaceSpace(s))

        # return s.replace(" ", "%20")
