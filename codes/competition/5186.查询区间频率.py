# -*- coding: utf-8 -*-
# @Time : 2021/11/21 11:33
# @Author : XDD
# @File : 5186.查询区间频率.py
import copy
class RangeFreqQuery:

    def __init__(self, arr):

        self.dp = [{} for i in range(len(arr))]
        for i in range(len(arr)):
            self.dp[i] = copy.copy(self.dp[i - 1])
            if arr[i] in self.dp[i]:
                self.dp[i][arr[i]] += 1
            else:
                self.dp[i][arr[i]] = 1

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.dp[right]:
            return 0
        elif value not in self.dp[left]:
            return self.dp[right][value]
        else:
            return  self.dp[right][value] - self.dp[left][right]






list = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]

a = RangeFreqQuery(list)
a.query(1, 2, 4)
