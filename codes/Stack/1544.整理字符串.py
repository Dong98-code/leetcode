class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for letter in s[1:]:
            if abs(ord(stack[-1])-ord(letter)) == 32:
                stack.pop()
            else:
                stack.append(letter)
        return ''.join(stack)

if __name__ == "__main__":
    solution = Solution()
    string = "leEeetcode"
    print(solution.makeGood(string))
