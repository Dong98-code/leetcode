class Solution:
    def generateMatrix(self, n: int) :
        res = [[0]*n for _ in range(n)]
        l, t = 0, 0
        r, b = n-1, n-1 # left, top, right, bottom
        num = 1
        while l <= r and t <= b:
            for j in range(l, r+1):
                res[t][j] = num
                num += 1
            for i in range(t+1, b+1):
                res[i][r] = num
                num += 1
            if l < r and t < b:
                for j in range(r-1, l-1, -1):
                    res[b][j] = num
                    num += 1
                for i in range(b-1, t, -1):
                    res[i][l] = num
                    num += 1
            l += 1
            r -= 1
            t += 1
            b -= 1
        return res
sol = Solution()
print(sol.generateMatrix(1))
