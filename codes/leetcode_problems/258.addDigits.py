class Solution:
    def addDigits(self, num: int) -> int:
        # if num == 0:
        #     return 0

        # return (num - 1) % 9 + 1
        while num >= 10:
            # next = 0
            # while (num != 0):
            #     next = next + num % 10
            #     num //= 10
            # num = next
            x = num // 10
            y = num % 10
            num = x + y
        return num


sol = Solution()
print(sol.addDigits(38))
