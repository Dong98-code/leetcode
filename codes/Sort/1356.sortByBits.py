class Solution:
    def sortByBits(self, arr):
        def count(num):
            ct = 0
            while num:
                ct += num & 1
                num = num >> 1
            return ct
        sort = sorted(arr, key = lambda i : count(i))
        return sort

if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    solution = Solution()
    print(solution.sortByBits(arr))

