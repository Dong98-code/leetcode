# -*- coding: utf-8 -*-
# @Time : 2021/7/23 11:02
# @Author : XDD
# @File : 1893.isCoverd.py
class Solution:
    def isCovered(self, ranges, left: int, right: int) -> bool:

        ranges.sort(key=lambda x: x[0])
        for range in ranges:
            l = range[0]
            r = range[-1]
            if l <= left and r >= left:
                left = r + 1
            if left > right :
                return True
        return False

ranges =  [[21,30], [10,20]]
left = 21
right = 21

sol = Solution()
print(sol.isCovered(ranges, left, right))
