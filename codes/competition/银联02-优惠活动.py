# -*- coding: utf-8 -*-
# @Time : 2022/3/15 16:14
# @Author : XDD
# @File : 银联02-优惠活动.py.py
from collections import Counter
class DiscountSystem:

    def __init__(self):
        self.acts = {}  # 存放现在的活动， key为actid ，values为对象

    def addActivity(self, actId: int, priceLimit: int, discount: int, number: int, userLimit: int) -> None:
        self.acts[actId] = [priceLimit, discount, number, userLimit, Counter()]  # 计数器用于记录参加的顾客的参与次数

    def removeActivity(self, actId: int) -> None:
        self.acts.pop(actId)

    def consume(self, userId: int, cost: int) -> int:
        # 查询当前的活动 / 可以参加的活动， 名额数
        # 查询可以参加的活动 中 已参加的而次数
        d = 0
        a = None
        for actId in self.acts.keys():
            if cost < self.acts[actId][0]:
                continue
            if self.acts[actId][2] <= 0:
                continue  # 次数不够用
            if self.acts[actId][-1][userId] > self.acts[actId][-2]:
                continue

            cur_d = self.acts[actId][1]
            if cur_d > d or (cur_d == d and actId < a):
                d = cur_d
                a = actId
        if a is not None:
            self.acts[a][-1][userId] += 1
            self.acts[a][-2] -= 1

        return cost - d


dis_count = DiscountSystem()
dis_count.addActivity(1,10,6,3,2)
dis_count.addActivity(2,15,8,8,2)
dis_count.consume(101, 13)
dis_count.consume(101, 17)



