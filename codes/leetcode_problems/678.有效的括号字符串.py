class Solution:
    def checkValidString(self, s: str) -> bool:
        # 栈
        stack_left = []
        stack_star = []
        for i in range(len(s)):
            if s[i] == "(":
                stack_left.append(i)
            elif s[i] == "*":
                stack_star.append(i)
            else:
                if not stack_star and not stack_left:
                    return False
                elif stack_left:
                    stack_left.pop()
                else:
                    stack_star.pop()
        # 判断栈中的序号’
        while stack_left and stack_star:
            if stack_star[-1] < stack_left[-1]:
                return False
            stack_left.pop()
            stack_star.pop()

        return len(stack_left) == 0

sol = Solution()
print(sol.checkValidString('()()*)'))
