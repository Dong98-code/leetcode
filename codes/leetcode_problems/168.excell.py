class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber:
            columnNumber -= 1
            s = chr(columnNumber%26+65)+s
            columnNumber //=26


        return s
s = Solution()
c = s.convertToTitle(1000)




