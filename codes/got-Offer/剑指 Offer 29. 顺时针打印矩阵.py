matrix = [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def spiralOrder(self, matrix):
        x, y =len(matrix), len(matrix[0])
        ans = []
        left ,right, top, bottom = 0, y-1, 0,x-1
        while left <= right and top <= bottom:
            for col in range(left, right+1):
                ans.append(matrix[top][col])
            for row in range(top+1, bottom+1):
                ans.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right-1, left-1, -1):
                    ans.append(matrix[bottom][col])
                for row in range(bottom-1, top, -1):
                    ans.append(matrix[row][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return ans

sol = Solution()
print(sol.spiralOrder(matrix))
