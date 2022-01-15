# -*- coding: utf-8 -*-
# @Time : 2022/1/15 21:47
# @Author : XDD
# @File : 373.查找和最小的k对数字.py
import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        # 小根堆
        m = len(nums1)
        n = len(nums2)
        hp = [(nums1[i] + nums2[0], i, 0) for i in range(m)]
        heapq.heapify(hp)

        res = []

        while hp and len(res) < k:
            _, i, j = heapq.heappop(hp)  # pop出最小的值
            res.append([nums1[i], nums2[j]])

            # 将 i+1,j 对应的值加入到队列中
            if j+1 < n:
                heapq.heappush(hp, (nums1[i]+nums2[j+1], i, j+1))
        return res


nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
sol = Solution()
print(sol.kSmallestPairs(nums1, nums2, k))
