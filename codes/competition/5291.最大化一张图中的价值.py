# -*- coding: utf-8 -*-
# @Time : 2021/11/7 15:25
# @Author : XDD
# @File : 5291.最大化一张图中的价值.py
from collections import  defaultdict
from collections import deque
# class Solution:
#     def maximalPathQuality(self, values, edges, maxTime: int) -> int:
#         graph = defaultdict(list)
#         for u, v, t in edges:
#             graph[u].append((v, t))
#             graph[v].append((u, t))
#
#         max_values = [values[0]]
#         visited = [0] * len(values)
#         visited[0] = 1
#
#         def dfs(node=0, ans=values[0], time=maxTime):
#             for v, t in graph[node]:
#                 if time < t:
#                     continue  # time为遍历一个节点后剩余的时间
#                 if not visited[v]:  # 节点价值最多算进总价值的一次
#                     ans += values[v]
#                 if not v:  # 此时v为0， 返回原始节点
#                     max_values[0] = max(ans, max_values[0])
#                 visited[v] += 1
#                 dfs(v, ans, time - t)
#                 visited[v] -= 1
#                 if not visited[v]:
#                     ans -= values[v]
#
#         dfs()
#         return max_values[0]
class Solution:
    def maximalPathQuality(self, values, edges, maxTime: int) -> int:
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        if not graph[0]:
            return values[0]  # 此时没有与其实节点相连的节点，只能返回其本身的价值

        ans = 0

        visited = [0] * len(values)
        visited[0] = 1
        q = deque()
        q.append((0, values[0], maxTime, [0]))
        while q:
            cur, v, tleft, path = q.popleft()
            if cur == 0:
                ans = max(ans, v)
            for nxt, t in graph[cur]:
                if tleft >= t:
                    path_new = path[:]
                    path_new.append(nxt)
                    if nxt in path:
                        q.append((nxt, v, tleft - t, path_new))
                    else:
                        q.append((nxt, v + values[nxt], tleft - t, path_new))
        return ans

values = [0,32,10,43]
edges = [[0,1,10],[1,2,15],[0,3,10]]
maxTime = 49

sol = Solution()
print(sol.maximalPathQuality(values, edges, maxTime))
