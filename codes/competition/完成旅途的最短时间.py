# -*- coding: utf-8 -*-
# @Time : 2022/2/27 11:21
# @Author : XDD
# @File : 完成旅途的最短时间.py
import math


class Solution:
    def minimumTime(self, time, totalTrips: int) -> int:
        l = 0
        min_t = min(time)
        time.sort()

        r = totalTrips * min_t
        res = 0
        while l < r - 1:
            cnt = 0
            mid = (r - l) // 2 + l

            for t in time:
                if t > mid:
                    break

                cnt += mid // t
            if cnt >= totalTrips:
                r = mid
            elif cnt < totalTrips:
                l = mid

        res = l
        return res

sol = Solution()

time = [5,10,10]
totalTrips = 9

sol.minimumTime(time, totalTrips)
