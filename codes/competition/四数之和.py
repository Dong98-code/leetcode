# -*- coding: utf-8 -*-
# @Time : 2021/9/5 11:31
# @Author : XDD
# @File : 四数之和.py
class Solution:
    def countQuadruplets(self, nums) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n - 1, 2, -1):
            # 求三数之和
            for j in range(0, i - 2):
                left = j + 1
                right = i - 1
                while left < right:

                    t_sum = nums[j] + nums[left] + nums[right]
                    if t_sum == nums[i]:
                        res += 1
                        right -= 1
                    elif t_sum > nums[i]:
                        right -= 1
                    else:
                        left += 1
        return res

sol = Solution()
print(sol.countQuadruplets([1,1,1,3,5]))
