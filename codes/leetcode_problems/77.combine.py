class Solution:
    def combine(self, n: int, k: int):
        path = []
        res = []

        def backtrack(n, start_index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start_index, n):
                path.append(i+1)
                backtrack(n, i+1)
                path.pop()

        backtrack(4, 0)
        return res
sol = Solution()
print(sol.combine(4,0))
