class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        def f(str_list):
            stack = []
            for item in str_list:
                if not stack and item == "#":
                    continue
                else:
                    if item == "#":
                        stack.pop()
                    else:
                        stack.append(item)
                # stack.append(item)
            return stack
        return f(s_list) == f(t_list)

if __name__ == "__main__":
    s = Solution()
    S ="ab##"
    T ="c#d#"
    # S = "ab##"
    # T = "c#d#"
    s.backspaceCompare(S, T)
