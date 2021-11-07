# -*- coding: utf-8 -*-
# @Time : 2021/11/7 15:25
# @Author : XDD
# @File : 5291.最大化一张图中的价值.py
from collections import  defaultdict
class Solution:
    def maximalPathQuality(self, values, edges, maxTime: int) -> int:
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        max_values = [values[0]]
        visited = [0] * len(values)
        visited[0] = 1

        def dfs(node=0, ans=values[0], time=maxTime):
            for v, t in graph[node]:
                if time < t:
                    continue  # time为遍历一个节点后剩余的时间
                if not visited[v]:  # 节点价值最多算进总价值的一次
                    ans += values[v]
                if not v:  # 此时v为0， 返回原始节点
                    max_values[0] = max(ans, max_values[0])
                visited[v] += 1
                dfs(v, ans, time - t)
                visited[v] -= 1
                if not visited[v]:
                    ans -= values[v]

        dfs()
        return max_values[0]

values = [0,32,10,43]
edges = [[0,1,10],[1,2,15],[0,3,10]]
maxTime = 49

sol = Solution()
print(sol.maximalPathQuality(values, edges, maxTime))
