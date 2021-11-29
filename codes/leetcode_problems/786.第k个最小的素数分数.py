# -*- coding: utf-8 -*-
# @Time : 2021/11/29 9:54
# @Author : XDD
# @File : 786.第k个最小的素数分数.py
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int):
        q = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                heapq.heappush(q, (arr[i] / arr[j], [arr[i], arr[j]]))

        # res = heapq.nsmallest(k, q)[-1][-1]
        res = q[k-1][-1]
        return res

arr=[1,2,3,5,7,11,13,17]
k=3
sol = Solution()
print(sol.kthSmallestPrimeFraction(arr, k))
