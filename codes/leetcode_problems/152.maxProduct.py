# -*- coding: utf-8 -*-
# @Time : 2021/7/25 14:02
# @Author : XDD
# @File : 152.maxProduct.py
class Solution:
    def maxProduct(self, nums) -> int:
        # 最大值和最小值都需要考虑
        n = len(nums)
        min_pre, max_pre = 1, 1
        res = -float("inf")
        for i in range(n):
            min_tmp = min_pre * nums[i]
            max_tmp = max_pre * nums[i]
            min_pre = min(nums[i], min(min_tmp, max_tmp))
            max_pre = max(nums[i], max(min_tmp, max_tmp))

            res = max(res, max_pre)

        return res

nums = [-2, 0, -1]
sol = Solution()
print(sol.maxProduct(nums))
