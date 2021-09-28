"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



示例:

输入
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
"""
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        H = [(2, 2), (3, 3), (5, 5)]
        heapq.heapify(H)
        for i in range(n - 1):
            num, p = heapq.heappop(H)
            heapq.heappush(H, (num * 2, 2))
            if p >= 3:
                heapq.heappush(H, (num * 3, 3))
                if p >= 5:
                    heapq.heappush(H, (num * 5, 5))
        #print(len(H)) #n = 1670时, H长度为162
        return num

sol = Solution()
print(sol.nthUglyNumber(10))
