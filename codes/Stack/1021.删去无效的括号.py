class Solution:
    def removeOuterParentheses(self, s):
        count = 0
        ans = ""
        for j in list(s):
            if j == '(':
                if count > 0:
                    ans = ans+j
                count += 1
            else:
                if count > 1:
                    ans += j
                count -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    string = "(()())(())"
    solution.removeOuterParentheses(string)
