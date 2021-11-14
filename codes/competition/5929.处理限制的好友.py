# -*- coding: utf-8 -*-
# @Time : 2021/11/14 12:57
# @Author : XDD
# @File : 5929.处理限制的好友.py
from collections import defaultdict


class Solution:
    def friendRequests(self, n: int, restrictions, requests):
        fa = list(range(n))
        # 某人的敌人
        cant = defaultdict(set)
        # 某个朋友圈的所有人员
        folks = defaultdict(set)
        # 某个朋友圈的所有人员的所有敌人
        enemies = defaultdict(set)

        def find_root(x):
            if fa[x] != x:
                fa[x] = find_root(fa[x])
            return fa[x]

        def merge(x, y):
            rx = find_root(x)
            ry = find_root(y)
            # 已是好友 or 在一个朋友圈内
            if rx == ry:
                return True
            # 分别更新当前 x，y 朋友圈的信息
            folks[rx].add(x)
            folks[ry].add(y)
            enemies[rx].update(cant[x])
            enemies[ry].update(cant[y])
            # 双方朋友圈的人都不是对方朋友圈的敌人，无内鬼
            if folks[rx].isdisjoint(enemies[ry]) and folks[ry].isdisjoint(enemies[rx]):
                # 交个朋友吧！
                fa[rx] = ry
                # 合并朋友圈信息
                folks[ry].update(folks[rx])
                enemies[ry].update(enemies[rx])
                return True
            return False

        for u, v in restrictions:
            cant[u].add(v)
            cant[v].add(u)

        res = []
        for u, v in requests:
            res.append(merge(u, v))

        return res

n = 5
restrictions = [[0,1],[1,2],[2,3]]
requests = [[0,4],[1,2],[3,1],[3,4]]
sol = Solution()
print(sol.friendRequests(n, restrictions, requests))
