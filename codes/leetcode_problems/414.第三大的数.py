# -*- coding: utf-8 -*-
# @Time : 2021/10/6 12:51
# @Author : XDD
# @File : 414.第三大的数.py
class Solution:
    def thirdMax(self, nums) -> int:
        n = len(nums)
        # a b 用于记录 第一大和第二大的数
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        a = -float('inf')
        b = -float('inf')
        c = -float('inf')
        for i in range(n):
            if nums[i] == a or nums[i] == b or nums[i] == c:
                continue
            elif nums[i] > a:
                c = b
                b = a  # 第一大变第二大，第二大变第三大
                a = nums[i]
            elif nums[i] > b :
                c = b
                b = nums[i]
            elif nums[i] > c:
                c = nums[i]
            else:
                continue
        return a if c == -float('inf') else c


sol = Solution()
nums = [1,2,-2147483648]

print(sol.thirdMax(nums))
