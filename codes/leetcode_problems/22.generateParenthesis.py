class Solution:
    def generateParenthesis(self, n: int):
        # ans = []
        # def backtrack(S, left, right):
        #     if len(S) == 2 * n:
        #         ans.append(''.join(S))
        #         return
        #     if left < n:
        #         S.append('(')
        #         backtrack(S, left+1, right)
        #         S.pop()
        #     if right < left:
        #         S.append(')')
        #         backtrack(S, left, right+1)
        #         S.pop()
        #
        # backtrack([], 0, 0)
        # return ans
        res = []

        def backtrack(path, l, r):
            # path为路径, l , r 为左右括号使用的数目
            if len(path) == 2 * n:
                return res.append("".join(path))
            if l < n:
                path.append("(")
                backtrack(path, l + 1, r)
                path.pop()
            if r < l:
                path.append(")")
                backtrack(path, l, r + 1)
                path.pop()

        backtrack([], 0, 0)
        return res
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
sol = Solution()
print(sol.generateParenthesis(3))
