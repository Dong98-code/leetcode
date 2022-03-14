# -*- coding: utf-8 -*-
# @Time : 2022/3/13 14:04
# @Author : XDD
# @File : 6032.得到要求路径的最小带权子图.py
from collections import defaultdict
import heapq
class Solution:
    def minimumWeight(self, n: int, edges, src1: int, src2: int, dest: int) -> int:
        # 最短路
        # 迪杰斯特 到其他节点的最短路之和
        # 3次

        # 第一步建图
        def dijkstra(n, g, start):

            dis = dict((key, INF) for key in range(n))
            dis[start] = 0
            vis = dict((key, False) for key in range(n))  # 标记是否访问过
            pq = []
            heapq.heappush(pq, [dis[start], start])

            while len(pq) > 0:
                v_dis, v = heapq.heappop(pq)  # 为访问节点中 距离最小的点和对应的距离
                if vis[v] == True:
                    continue
                vis[v] = True
                for node in g[v]:  # 与v直接相连的点
                    new_dis = dis[v] + int(g[v][node])
                    if new_dis < dis[node] and (not vis[node]):  # 如果与v直接相连的node通过v到src的距离小于dis中对应的node的值        ,则用小的值替换
                        dis[node] = new_dis  # 更新点的距离
                        #  dis_un[node][0] = new_dis    #更新未访问的点到start的距离
                        heapq.heappush(pq, [dis[node], node])
            return dis

        INF = 999999999
        graph_1 = defaultdict(lambda: defaultdict(lambda :INF))  # 正向图
        graph_2 = defaultdict(lambda: defaultdict(lambda :INF))  # 反向图

        for u, v, w in edges:
            graph_1[u][v] = min(graph_1[u][v], w)
            graph_2[v][u] = min(graph_2[v][u], w)

        dis_x = dijkstra(n, graph_1, src1)
        dis_y = dijkstra(n, graph_1, src2)
        dis_z = dijkstra(n, graph_2, dest)
        res = INF
        res = min(dis_x[i] + dis_y[i] + dis_z[i] for i in range(n))
        return -1 if res == INF else res


n = 6
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5


sol = Solution()
print(sol.minimumWeight(n, edges, src1=src1, src2=src2, dest=dest))
