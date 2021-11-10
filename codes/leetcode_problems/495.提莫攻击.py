# -*- coding: utf-8 -*-
# @Time : 2021/11/10 10:52
# @Author : XDD
# @File : 495.提莫攻击.py
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        res = 0
        for i in range(len(timeSeries)):
            if i == 0:
                continue
            else:
                res += min(timeSeries[i] - timeSeries[i - 1], duration)
        res += duration  # 最后一次攻击

        return res
