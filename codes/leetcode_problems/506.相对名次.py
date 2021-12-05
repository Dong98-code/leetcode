# -*- coding: utf-8 -*-
# @Time : 2021/12/2 10:35
# @Author : XDD
# @File : 506.相对名次.py
import heapq
class Solution:
    def findRelativeRanks(self, score):
        # heapq ，讲值与其索引存入一个heap，每次弹出的都是最大的值
        h = []
        # 放入队列
        for i in range(len(score)):
            heapq.heappush(h, (score[i], i))

        # 去除队列
        ans = ['' for _ in range(len(score))]
        r = len(score)
        while h:
            _, idx = heapq.heappop(h)
            if r == 1:
                ans[idx] = 'Gold Medal'
            elif r == 2:
                ans[idx] = 'Silver Medal'
            elif r == 3:
                ans[idx] = 'Bronze Medal'
            else:
                ans[idx] = str(r)

            r -= 1
        return ans

sol = Solution()
score = [10,3,8,9,4]
print(sol.findRelativeRanks(score))
