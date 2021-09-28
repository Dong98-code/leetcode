"""
寻找质数

"""
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         # 埃式筛选
#         cnt = 0
#         if n == 0 or n == 1:
#             return 0
#         b = [1 for i in range(n)]
#         b[0] = b[1] = 0
#         for i in range(2, n):
#             if b[i]:
#                 cnt += 1
#                 j = i*2
#                 while j < n:
#                     b[j] = 0
#                     j = j + i
#         return cnt
#     #  改进， 所有大于3的数都可以表示为（6k+-1）
#     #     b = [0]*n
#     #     for i in range(n):
#     #         if (i+1)%6 or (i-1)%6 == 0:
#     #             b[i] =

class Solution:
    def countPrimes(self, n: int) -> int:
        n -= 1
        if n < 2:
            return 0
        r = int(n ** 0.5)
        V = [n // d for d in range(1, r + 1)]
        V += list(range(V[-1] - 1, 0, -1))

        S = {v: v - 1 for v in V}
        # print(S)
        for p in range(2, r + 1):
            if S[p] == S[p - 1]:
                continue
            p2 = p * p
            sp_1 = S[p - 1]
            for v in V:
                if v < p2:
                    break
                S[v] -= S[v // p] - sp_1
            # print(S)
        return S[n]


# 作者：lihaitao1986
# 链接：https: // leetcode - cn.com / problems / count - primes / solution / shi - jian - fu - za - du - wei - on075de - jie - fa - ji - 9
# qmi6 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


sol = Solution()
print(sol.countPrimes(100))
