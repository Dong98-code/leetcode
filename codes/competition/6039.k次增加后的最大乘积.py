# -*- coding: utf-8 -*-
# @Time : 2022/4/10 11:42
# @Author : XDD
# @File : 6039.k次增加后的最大乘积.py
import heapq
from collections import Counter
class Solution:
    def maximumProduct(self, nums, k: int) -> int:
        # 每次都将最小值增加1
        cnt = Counter(nums)
        if cnt[0] > k:
            return 0
        heapq.heapify(nums)
        while k > 0:
            k -= 1
            min_num = heapq.heappop(nums)
            min_num += 1
            heapq.heappush(nums, min_num)

        res = 1
        for num in nums:
            res = res * num
        return res % 1000000007

sol = Solution()
print(sol.maximumProduct(nums=[6,3,3,2], k=2))
