class Solution:
    def largestOddNumber(self, num: str) -> str:
        j = len(num)-1
        while j>=0:
            if int(num[j])%2 == 1:
               return num[:j+1]
            else:
                j -= 1
        return ''

sol = Solution()
print(sol.largestOddNumber("35427"))
