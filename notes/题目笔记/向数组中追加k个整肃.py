# -*- coding: utf-8 -*-
# @Time : 2022/3/6 14:43
# @Author : XDD
# @File : 向数组中追加k个整肃.py
class Solution:
    def minimalKSum(self, nums, k) -> int:

        nums = sorted(set(nums)) + [int(2e9)]
        s = 0
        for i, num in enumerate(nums):
            if num - 1 - i >= k:
                return (k + i) * (k + i + 1) // 2 - s
            s += num

        return -1


sol = Solution()
print(sol.minimalKSum(nums=[1], k=100000000))
