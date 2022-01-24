# -*- coding: utf-8 -*-
# @Time : 2022/1/24 16:54
# @Author : XDD
# @File : 2045.到达目的地的第二短路径.py
import collections
class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:
        # 第一步建图
        graph = [[] for _ in range(n + 1)]  # 索引为节点，从1开始
        for edge in edges:
            t, h = edge  # tail -> head
            graph[t].append(h)
            graph[h].append(t)

        q = collections.deque()
        q.append((1, 0))  # node,  dist
        dists = [[float('inf')] * 2 for _ in range(n + 1)]

        while dists[n][1] == float('inf'):
            t, dis = q.popleft()
            for h in graph[t]:
                if dis+1 < dists[h][0]:
                    # 第一次经过
                    dists[h][0] = dis+1
                    q.append((h, dis+1))
                elif dists[h][0] < dis+1 < dists[h][1]:
                    dists[h][1] = dis+1
                    q.append((h, dis+1))

        res = 0
        for _ in range(dists[n][1]):
            if res % (2 * change) >= change:
                res += 2 * change - res % (change * 2)
            res += time
        return res

n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5

sol = Solution()
print(sol.secondMinimum(n, edges, time, change))
