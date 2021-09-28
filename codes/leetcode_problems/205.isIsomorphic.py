"""
给定两个字符串s和t，判断它们是否是同构的。

如果s中的字符可以按某种映射关系替换得到t，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，
字符可以映射到自己本身。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # flag = True
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        dic = {}
        dic2 = {}
        for i in range(l1):
            if s[i] not in dic:
                dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        for j in range(len(t)):
            if t[j] not in dic2:
                dic2[t[j]] = s[j]
            else:
                if dic2[t[j]] != s[j]:
                    return False
        return True


s = "badc"
t = "baba"
sol = Solution()
print(sol.isIsomorphic(s, t))
